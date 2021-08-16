// window.onload = function() {
//     alert("Page is loaded");
// }

// variable types
var wild = "wild variable";
let reasonable = 5;
const stubborn = -1.5;

//object example
let person = {};
person = {
    'name': 'benton',
    'age': 38,
    'code': ["cpp", "c#", "javascript"]
}

console.log("for loop:");
for (let i = 0; i < person.code.length; i++){
    console.log(person.code[i]);
}

console.log("\nfor each loop:");
person.code.forEach(str => {
    console.log(str);
});

console.log("\npop");
let js = person.code.pop();
console.log(js);
//grab a node
const element = document.getElementById("grab-example");


element.innerText = "this instead";
element.innerHTML = "this <strong>instead</strong>";

// both are valid accessors for ojects
element.innerText = person["name"] + " " + person["code"];
element.innerText = person.name + " " + person.code[0];

console.log("person is a " + typeof(person.code));
console.log("person.code is a " + typeof(person.code));
console.log("person.code[1] is a " + typeof(person.code[1]));
console.log("wild is a " + typeof(wild));

// new concantenation
let num = "3";
num = Number(num) + 3;
console.log(`number typecast: ${typeof(num)}`);
// newlines are displayed
console.log(`number typecast:
${num}`);
num = Object(num);
console.log(`number typecast: ${typeof(num)}`);
num += 3;
console.log(`number typecast: ${num}`);

// selecting class nodes
const node = document.querySelector(".classy");
console.log(`query selector: ${node.innerText}`);
const nodes = document.querySelectorAll(".classy");
console.log(`multiple query selector: ${nodes[1].innerText}`);

// editing class nodes
console.log("editing nodes")
const items = document.querySelectorAll("li");
items.forEach(node => {
    node.innerText = "changed";
    console.log(node.innerText);
});
// foreach iterator
console.log("foreach iterator")
items.forEach((node, index) => {
    node.innerText = `changed ${index}`
    console.log(node.innerText);
});

// functions
function multiplyNums(numA, numB) {
    return numA * numB;
}
numC = multiplyNums(5, 6);
console.log(`function return value: ${numC}`);

// rest operator and for...of loop
function stringToList(...strings) {
    let arr = [];
    for(let s of strings) {
        arr.push(s);
    }
    return arr;
}

let arr = stringToList("1", "apple", "3.4");

arr.forEach(s => {
    console.log(s);
});


// window.onbeforeunload = function() {
//     console.log("Before unload"); // necessary to pause leaving
//     // alert("you are leaving the page");
//     return "you are leaving the page";
// }

// example of built-in callback
setTimeout(function() {
    console.log("delayed text");
}, 2500);

console.log("immediate text");

// delete object property
const car = {
    'make': 'ford',
    'model': 'fiesta'
}
console.log(car);
delete car['model'];
console.log(car);

let apiNum = prompt("Enter number from 1 - 50");
let starChar;
apiNum = "https://swapi.dev/api/people/" + apiNum +"/";
console.log(apiNum);

// fetch API
fetch(apiNum)
    .then(response => response.json())
    .then(data => {
        starChar = data;
        console.log(starChar.name);
        character.innerText = starChar.name;
    });

// interesting: this doesn't work because it executes before fetch returns
// console.log(starChar["name"]);