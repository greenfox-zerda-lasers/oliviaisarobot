var asteroidList = document.querySelector('ul.asteroids');

var newAsteroidGreenFox = document.createElement('li');
newAsteroidGreenFox.textContent = 'The Green Fox';
asteroidList.appendChild(newAsteroidGreenFox);

var newAsteroidLamplighter = document.createElement('li');
newAsteroidLamplighter.textContent = 'The Lamplighter';
asteroidList.appendChild(newAsteroidLamplighter);

var container = document.querySelector('div.container');

var newHeading = document.createElement('h1');
newHeading.textContent = 'I can add elements to the DOM!';
container.appendChild(newHeading);
