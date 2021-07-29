"use strict"

function GenRandApiReq() {
    let randNum = Math.ceil(Math.random() * 83);
    let fetchApi = `https://swapi.dev/api/people/${randNum}/`
    return fetchApi;
}

function GetIds() {
    nameId = document.querySelector(".character__name");
    valueIds = document.querySelectorAll(".character__values > div");
}

async function GetData(address) {
    const response = await fetch(address);
    const json = await response.json();
    return json;
}

async function CleanData(origData) {
    for (const [key, value] of Object.entries(origData)) {
        // look for arrays
        if (Array.isArray(value)) {
            for (const [i, element] of value.entries()) {
                // look for links inside arrays
                if (element.indexOf("https") != -1) {
                    const newData = await GetData(element);
                    // replace link with name or title
                    if (newData["name"] !== undefined) {
                        origData[key][i] = newData["name"]
                    } else if (newData["title"] !== undefined) {
                        origData[key][i] = newData["title"];
                    }
                }
            };
        }
        // look for links and replace with name
        if (value.indexOf("https") != -1) {
            const newData = await GetData(value);
            origData[key] = newData["name"];
        }
    }
    return origData;
}

function PopulateFields(fieldData) {
    nameId.innerText = fieldData["name"];
    valueIds.forEach(node => {
        const nodeId = node.id;
        node.innerText = fieldData[nodeId];
    });
}

// begin execution
let nameId;
let valueIds;
GetIds();

// lambda function is necessary to avoid function firing automatically
document.getElementById("random-button").addEventListener(
    "click", async () => {
        let apiUrl = GenRandApiReq();
        let data = await GetData(apiUrl);
        data = await CleanData(data);
    PopulateFields(data);
});