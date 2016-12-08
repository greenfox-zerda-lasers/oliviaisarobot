var button = document.querySelector('button');
var itemList = document.querySelectorAll('li');
var result = document.querySelector('p');

function countTheItems() {
  result.innerHTML = itemList.length;
}

button.addEventListener('click', countTheItems);
