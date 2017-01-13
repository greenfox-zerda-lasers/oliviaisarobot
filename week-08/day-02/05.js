// Add a click event listener to a <button> and console.log its innerHTML

var myButton = document.getElementById('nice-button');

function logThis() {
  console.log(myButton.innerHTML);
}

myButton.addEventListener('click', logThis);
