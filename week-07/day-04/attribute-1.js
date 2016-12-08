var imageUrl = document.querySelector('img');

console.log(imageUrl.getAttribute('src'));

imageUrl.setAttribute('src', 'http://www.thisiscolossal.com/wp-content/uploads/2011/06/5868078138_8aac2b7490_b.jpg');

var websiteUrl = document.querySelector('a');

websiteUrl.setAttribute('href', 'http://www.greenfoxacademy.com/');

var secondButton = document.getElementsByClassName('this-one');

secondButton[0].disabled = true;
secondButton[0].textContent = 'Don\'t click me!'
