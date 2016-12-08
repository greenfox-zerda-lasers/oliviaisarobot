var paragraphs = document.getElementsByTagName('p');
var secondParagraph = document.getElementsByClassName('output1')[0];
var thirdParagraph = document.getElementsByClassName('output2')[0];

secondParagraph.innerHTML = paragraphs[0].textContent;
thirdParagraph.innerHTML = paragraphs[0].innerHTML;
