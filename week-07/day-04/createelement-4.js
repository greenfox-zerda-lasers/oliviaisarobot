var asteroidList = document.querySelector('ul.asteroids');
var king = document.querySelector('li');

asteroidList.removeChild(king);

for (var i = 0; i < planetData.length; i++) {
  var newListItem = document.createElement('li');
  newListItem.textContent = planetData[i].content;
  if (planetData[i].asteroid) {
    asteroidList.appendChild(newListItem);
  }
}
