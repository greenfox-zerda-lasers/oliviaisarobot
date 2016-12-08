var asteroidList = document.querySelector('ul.asteroids');
var king = document.querySelector('li');

asteroidList.removeChild(king);

for (var i = 0; i < 3; i++) {
  var newListItem = document.createElement('li');
  newListItem.textContent = 'The Fox';
  asteroidList.appendChild(newListItem);
}
