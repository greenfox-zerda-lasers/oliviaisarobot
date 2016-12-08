var paragraphs = document.getElementsByTagName('p');

for (var i = 0; i < paragraphs.length; i++) {
  paragraphs[i].innerHTML = paragraphs[paragraphs.length - 1].innerHTML;
}
