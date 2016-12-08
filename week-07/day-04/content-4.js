var myList = ['apple', 'banana', 'cat', 'dog'];

var listItems = document.querySelectorAll('li');

for (var i = 0; i < listItems.length; i++) {
  listItems[i].innerHTML = myList[i];
}
