/*
 *window is where the alert function comes from
 *we don't have to use window.func()
 *because it is at the very top level
 *window obj has the local storage object where we can store data on browser
 *it has the fetch api too
 */

console.log(window);
window.alert("how deep is your love is it like the ocean");

console.log(window.innerHeight, window.innerWidth);

// THE DOM is in window.document

// Single Element Selector
//?the good old getElementById(), only gets ids
const form1 = document.getElementById("a-form-id-maybe");

//? the newer querySelector()
//? can get anything: ids, classes
//? selects only one thing, the first one
const form2 = document.getElementById("#a-form-id-maybe");
const btn1 = document.querySelector(".class");
const btn2 = document.querySelector("h1");

// Multiple Element Selector

//? the recommended way to select, others are older
//? returns a NodeList object which is an iterable
const listItems = document.querySelectorAll(".item");
listItems.forEach((item) => item.firstChild);

// Manipulating the DOM
const ul = document.querySelector(`.items`);
ul.remove();
ul.lastElementChild().remove();
//? only get human readable elements
ul.children[1].innerText = "brad";
//? get all the text inside the element including script and style
ul.firstChild.textContent = "hello";
ul.lastElementChild.innerHTML = "<h1>Hello</h1>";
//? style manipulates the css
ul.style.background = "red";

//The Event Listener
//some events like:
// click, mousehover, mouseout
ul.addEventListener("click", (event) => {
  //? prevents the default action of the element
  event.preventDefault();
  //? gets the element of the event
  console.log(event.target.class);

  //? we changed the element by id's style's background attribute
  document.querySelector("#my-form").style.background = "#ccc";

  //?we added a class to an element to change the style
  document.querySelector("body").classList.add("bg-dark");

  document.querySelector(".items").lastElementChild.innerHTML =
    "<h1>YOU PRESSED</h1>";
});
