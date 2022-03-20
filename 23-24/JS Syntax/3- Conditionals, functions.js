//CONDITIONALS

const numero = "10";

//! NEVER USE THIS
if (numero == 10) {
  console.log("true");
}

if (numero === 10) {
  console.log("won't log because it's false");
} else if (numero < 10) {
  console.log("hot");
} else {
  console.log("bruh");
}
console.log(numero == 10, numero === 10);
//! IT WILL ONLY MATCH THE VALUE NOT THE VALUE "10"==10 returns true
//! HOWEVER "10"===10 returns false

//? now time for a ternary operator "?"
const color = numero > 0 ? "red" : "blue";
console.log(color);

switch (color) {
  case "blue":
    console.log("blue");
    break;
  case "red":
    console.log("red");
    break;
  default:
    console.log("another color");
    break;
}

////////////////////
//FUNCTIONS

function addNums(num1 = 0, num2 = 0) {
  return num1 + num2;
}

console.log(addNums((num1 = 4), (num2 = 3)));

//? arrow functions are like lambdas
//? and can be passed as arguments and such
const mulNums = (num1 = 0, num2 = 0) => {
  num1 * num2;
};

const someArrayWithArrowFunctions = someArray.map((num1 = 0) => num1 * 5);
console.log(someArrayWithArrowFunctions);
