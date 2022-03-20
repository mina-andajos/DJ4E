// alert("Yo you can use alert here too");
const x = 1 + 2;
console.log("hello", x);
console.error("THIS IS AN ERROR");
console.warn("THIS IS A WARNING");

//! var is global
//? use let, const instead

let y = 4; // it can change the value
const age = 50;
// age = 5;

//! always use const unless you know you will reassign the value

// const ag //? const declaration must have assigned values

let score;
score = 5; //? this can work

// primitive data types:
// string, number, boolean, null, undefined, symbol
const name = "john";
const num = 4;
const isCool = true;
const thereAreNoFloatsOrIntegersInJSJustNumbers = 5.5;
const hoe = null;
const anUndefinedVariable = undefined;
let anotherUndefinedVariable;

for (let variable of [
  name,
  num,
  isCool,
  thereAreNoFloatsOrIntegersInJSJustNumbers,
  hoe,
  anUndefinedVariable,
  anotherUndefinedVariable,
]) {
  console.log(typeof variable);
}
//! typeof not the python baddie func
//? you can notice that typeof shows null as "object" which is not true

//////////////////
// CONCATENATION AND TEMPLATE STRINGS

const txt1 = "woah";
const num5 = 5;

console.log("The old cringe way of concatenated text" + "" + txt1 + "" + num5);
console.log(
  `Now if U use back-ticks, it's a Template String. ${txt1}.\nand it has ${"\n"} too!\n${num5}`
);

const templateStringIsTheNewName = `wassup ${5 + 5}`;

const s = `Hello World`;
console.log(
  s,
  s.length,
  s.toUpperCase(),
  s.toLowerCase(),
  s.split(""),
  s.substring(0, 5).toLowerCase(),
  s.slice(0, 5)
);

//! slice works just like python
//! substring if it found min>max it will invert it
//! and if it finds a -ve num or Nan it will be treated as 0

/*
multi-line comments
multi
line
*/