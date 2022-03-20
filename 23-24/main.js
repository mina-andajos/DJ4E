//? getting the elements we want to manipulate by id
//! REMEMBER IT'S JUST THE ELEMENTS NOT THE VALUES
const myForm = document.querySelector("#my-form");
const nameInput = document.querySelector("#name");
const emailInput = document.querySelector("#email");
const userList = document.querySelector("#users");
//? getting the msg element by class
const msg = document.querySelector(".msg");

myForm.addEventListener("submit", onSubmit);
function onSubmit(event) {
  //? prevent the default behavior of the event
  event.preventDefault();

  //? if the name or email element values are empty on submit:
  if (nameInput.value === "" || emailInput.value === "") {
    //? add an error message by adding the error class to the msg element
    msg.classList.add("error");
    //? and adding html to it
    msg.innerHTML = "Please enter all fields";

    //? and waiting for 3000ms then removing the msg element
    setTimeout(() => msg.remove(), 3000);

    //? if all is good:
  } else {
    //? creating a list_item element
    const li = document.createElement("li");
    //? adding a child to the element
    li.appendChild(
      //? creating a text node that has a template string
      document.createTextNode(`${nameInput.value} : ${emailInput.value}`)
    );

    //? appending the list_item element as a child to the userList element
    userList.appendChild(li);

    //?clearing fields
    nameInput.value = "";
    emailInput.value = "";
  }
}
