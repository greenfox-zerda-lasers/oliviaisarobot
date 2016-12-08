var asteroidList = document.querySelector('ul.asteroids');
var king = document.querySelector('li');

asteroidList.removeChild(king);

var newListItems = ['apple', 'bubble', 'cat', 'green fox']

for (var i = 0; i < newListItems.length; i++) {
  var newListItem = document.createElement('li');
  newListItem.textContent = newListItems[i];
  asteroidList.appendChild(newListItem);
}
