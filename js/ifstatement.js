// exercise 1

let strictA = true;
let strictB = 1;
console.log(strictA == strictB); // true : value of true is the same as 1
console.log(strictA === strictB); // false : even though the same value the type differs

// exercise 2

console.log(strictA != strictB); // false
console.log(strictA !== strictB); // true

// exercise 3

let age = 50;

if (age >= 18 && age <= 65) {
    console.log(true);
} else if (age < 18) {
    console.log("underage")
} else {
    console.log(false)
}

// exercise 4

// let age = 40;

let result = age >= 50 ? "50 or over": "Under 50";
console.log(result);

// exercise 5

let day = 6;
switch (day) {
  case 0:
    console.log("sunday");
    break;
  case 1:
  case 2:
  case 3:
  case 4:
  case 5:
    console.log("weekday");
    break;
  case 6:
    console.log("saturday");
    break;
  default:
    console.log("not a valid day");
}