let a;
let b = "12345";
let c = 12344;
let d = true;
let e = {a:"JavaScript"};

console.log(typeof(a)); 
console.log(typeof(b));
console.log(typeof(c));
console.log(typeof(d));
console.log(typeof(e));

// undefined
// variables.js:8 string
// variables.js:9 number
// variables.js:10 boolean
// variables.js:11 object


let totalMoney = 4000;
let moneyPaidSoFar = 2348;
let totalLeftToPay;

console.log(`The total bill is £${totalMoney} the remaining amount of money to be paid is £${totalMoney - moneyPaidSoFar}`)


function sayHello() {
    return "Someone says hello";
  }

  console.log(sayHello())