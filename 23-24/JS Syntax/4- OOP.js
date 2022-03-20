//OOP

//!es5 functional constructor, not so good
function Person(firstName, lastName, dob) {
  this.firstName = firstName;
  this.lastName = lastName;
  this.dob = new Date(dob);
}
//? better to use prototypes
Person.prototype.getBirthYear = function () {
  return this.dob.getFullYear();
};
Person.prototype.getFullName = () => `${this.firstName} ${this.lastName}`;
//?instantiating through the function
const person1 = new Person("ahmed", "najjad", "5-6-2020");
console.log(person1.dob.getFullYear());

//! THE SUPERIOR ES6 CLASSES
class Human {
  constructor(firstName, lastName, dob) {
    this.firstName = firstName;
    this.lastName = lastName;
    this.dob = new Date(dob);
  }

  getBirthYear() {
    return this.dob.getFullYear();
  }

  getFullName() {
    return `${this.firstName} ${this.lastName} hello`;
  }
}
