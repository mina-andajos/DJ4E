// ARRAYS

const aBasicArrayMadeWithAConstructor = new Array(1, 2, 3); //? notice the "new" keyword
const anotherArray = ["apple", "orange"];
console.log(anotherArray, anotherArray[1]);
anotherArray[2] = "strawberry";
console.log(anotherArray[2]); //! IN CONST YOU CAN RUN METHODS AND CHANGE VALUES BUT YOU CAN'T REASSIGN IT AGAIN
anotherArray.push("hot"); //? adds to end
anotherArray.unshift("hot"); //? add to beginning
anotherArray.pop(); //? pops last element
console.log(Array.isArray(anotherArray), Array.isArray("fsf"));
console.log(anotherArray.indexOf("apple"));

/////////////////////////////////////////////////
// OBJECT LITERALS/
//better than dictionaries

const person = {
  firstName: "John",
  lastName: "Doe",
  age: 31,
  hobbies: ["music", "reading"],
  address: {
    street: "21 ahmad",
    city: "cairo",
    apartmentNumber: 13,
  },
};
person.email = "aaa@aaa.aaa";

console.log(person);
console.log(person.age, person.hobbies[0], person.address.apartmentNumber);
console.log(person.email);

//? new destructuring stuff
const {
  firstName,
  lastName,
  address: { city },
} = person;

arrayOfObjects = [
  person,
  {
    id: 1,
    text: "hello",
  },
];
console.log(arrayOfObjects[1].id);

//!JSON IS VERY SIMILAR BUT
//!OBJECT ATTRIBUTES ARE IN STRINGS (LIKE PYTHON DICTS)
//!NO SINGLE QUOTES ARE ALLOWED

const arrayOfObjectsJSON = JSON.stringify(arrayOfObjects);
console.log(arrayOfObjectsJSON);

////////////////////////////////
//LOOPS

for (let counter = 0; counter <= 10; counter++) {
  console.log(`Iteration number ${counter}`);
}

//? notice the use of let
let i = 5;
while (i > 0) {
  i--;
}

const someArray = [1, 2, 3, 4, 5, 6, 7];

//?cringiest way to loop
for (let counter = 0; counter < someArray.length; counter++) {
  console.log(counter);
}

//? notice the use of let
for (let element of someArray) {
  console.log(element);
}

///////////////////////////
//HIGH ORDER ARRAY METHODS
//forEach, map, filter

someArray.forEach(function (todo) {
  console.log(
    `That's some new way to loop an Array. it accepts at least a callback function like this, first param to add to it is ofc the item returned each iteration. ${todo}`
  );
});

const allNumbersAreMultipliedNow = someArray.map(function (todo) {
  console.log(
    `map returns an array of the callback function applied to the input array. similar to python ${todo}`
  );

  return todo * 2;
});
console.log(allNumbersAreMultipliedNow);

const onlyNumbersAboveTwo = someArray.filter(function aFunctionReturningBool(
  todo
) {
  console.log(
    `the callback function is the filter applied to the array, return another array ${todo}`
  );

  return todo > 2; //? always return a bool
});
console.log(onlyNumbersAboveTwo);

const onlyNumbersAboveTwoMultiplied = someArray
  .filter(function (todo) {
    return todo > 2; //? always return a bool
  })
  .map(function (todo) {
    return todo * 2;
  });
console.log(onlyNumbersAboveTwoMultiplied);
