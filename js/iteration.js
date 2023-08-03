// exercise 1

for (let A = 100; A <= 200; A++) {
    console.log(A)
    A++;
}

// // exercise 2

for (let A = 100; A <= 200; A++) {
    if (A % 2 == 0) {
        console.log("-");
    } else {
        console.log("*");
    }
}

// exercise 3

// loop to repeat the block of code
for (let j = 1; j < 11; j++) {
    // the block of code to repeat
    for (let i = 1; i < 11; i++) {
        console.log(j)
    }
}



// exercise 4 (since i've done for loops, i've now written some while loops)

let A = 100;
while (A <= 200) {
    A++;
    console.log(A);
}

let i = 100;
while (i <= 200) {
    if (i % 2 == 0){
        console.log("-");
    } else {
        console.log("*");
    }
    i++;
}
