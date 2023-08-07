"use strict"
// exercise 1
let func = (num1, num2) => num1 - num2;
console.log(func(5,2));

// OR
function func2(num1, num2) {
    return num1 - num2;
}
console.log(func2(5,2));

// exercise 2
let welcome = (yourname, age, gender) => `My name is ${yourname}, i am ${age} years old and of gender ${gender}.`;
console.log(welcome("Pam", 28, "female"));

// OR
const welcome2 = function(yourname, age, gender) {
    return console.log( `My name is ${yourname}, i am ${age} years old and of gender ${gender}.`)
}
console.log(welcome2("Pam", 28, "female"));

// exercise 3
let powerUp = (n1, n2) => Math.pow(n1,n2);

console.log(powerUp(2,3));
console.log(powerUp(3,3));