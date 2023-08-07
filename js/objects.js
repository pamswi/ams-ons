// exercise 1
let darthVader = {
    allegiance: "empire",
    weapon: "lightsaber",
    sith: true
};
console.log(darthVader);

// // exercise 2
console.log(`Darth Vader's allegiance is to the ${darthVader.allegiance}`);
console.log(`Darth Vader's weapon of choice is ${darthVader.weapon}`);
console.log(`Darth Vader is a sith? ${darthVader.sith}`);
console.log(`Darth Vader is a jedi? ${darthVader.sith ? "false" : "true"}`);

// exercise 3
let myArray = ["hello", "everyone..."];
console.log(myArray.length);
myArray.push("element1", "element2", "element3");
console.log(myArray.length);
myArray.shift();
console.log(myArray.length);
for (let item in myArray){
    console.log(myArray[item])
};