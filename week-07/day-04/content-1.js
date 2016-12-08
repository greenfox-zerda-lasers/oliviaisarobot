var heading = document.getElementsByTagName('h1');

alert(heading[0].textContent);

var paragraphs = document.getElementsByTagName('p');

console.log(paragraphs[0].textContent);

var secondParagraph = document.getElementsByClassName('other');

alert(secondParagraph[0].textContent);

var newHeading = document.getElementsByTagName('h1');
newHeading[0].innerHTML = "<h1>New content</h1>"

var lastParagraph = document.getElementsByClassName('result');
lastParagraph[0].innerHTML = paragraphs[0].textContent;
