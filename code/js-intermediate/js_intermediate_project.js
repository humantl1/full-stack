"use strict"

function GenRandApiReq() {
    let randNum = Math.ceil(Math.random() * 83);
    let fetchApi = `https://swapi.dev/api/people/${randNum}/`
    return fetchApi;
}

function GetIds() {
    button = document.querySelector("#random-button")
    nameId = document.querySelector(".character__name");
    valueIds = document.querySelectorAll(".character__values > div");
    attributeIds = document.querySelectorAll(
        ".character__attributes > div");
    for (let node of attributeIds) {
        attributeIdMap.set(node.id, node.innerText);
    }
}

async function GetData(address) {
    const response = await fetch(address, {
        method: 'GET'
    });
    const json = await response.json();
    return json;
}

// async function GetData(address) {
//     fetch(address)
//     .then(response => {
//         if (response.ok) {
//             return response.json();
//         }
//         return Promise.reject(response);
//     })
//     .then((result) => {
//         console.log(result);
//     })
//     .then((error) => {
//         console.warn('Network Error', error);
//     });
// }

function WipeData() {
    for (let node of valueIds) {
        node.innerText = "";
        node.style.height = "28px";
    }
    for (let node of attributeIds) {
        node.innerText = attributeIdMap.get(node.id);
        node.style.height = "28px";
    }
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

function ParseArray(node, attId, arr) {
    if (arr.length === 0) {
        node.innerText = 'N/A\n';
    } else {
        let attNode = document.querySelector(attId);
        let elementHeight = arr.length * 28;
        attNode.style.height = elementHeight + "px";
        node.style.height = elementHeight + "px";
        for(let element of arr) {
            node.innerText += `${element}\n`;
            // attNode.innerText += "\n";
        }
    }
}

function PopulateFields(fieldData) {
    nameId.innerText = fieldData["name"];
    valueIds.forEach(node => {
        let thisField = fieldData[node.id];
        let attId = "#" + node.id + "-att"
        console.log(attId);
        if (Array.isArray(thisField)) {
            ParseArray(node, attId, thisField);
        } else if (node.id === "height" && thisField !== "unknown") {
            node.innerText = thisField + " cm";
        } else if (node.id === "mass" && thisField !== "unknown") {
            node.innerText = thisField + " kg";
        } else {
            node.innerText = thisField;
        }
    });
}

// begin execution
let button;
let nameId;
let valueIds;
let attributeIds;
const attributeIdMap = new Map();
GetIds();

// lambda function is necessary to avoid function firing automatically
button.addEventListener(
    "click", async () => {
        button.innerText = "Loading"
        // let apiUrl = GenRandApiReq();
        let apiUrl = "https://swapi.dev/api/people/1/";
        let data = await GetData(apiUrl);
        data = await CleanData(data);
        WipeData();
        PopulateFields(data);
        button.innerText = "Random";
        // change populate fields for mobile devices
        // stack attribue over value, like:
        // Name:
        // Luke Skywalker
        // Height:
        // 172 cm ...
        // set timer to display timeout text if fetch > 10sec
});