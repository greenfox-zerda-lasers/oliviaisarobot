var paragraphs = document.querySelectorAll('p');

if (paragraphs[2].className === 'cat') {
  console.log('YEAH CAT!');
}

if (paragraphs[3].className === 'dolphin') {
  paragraphs[0].innerHTML = 'pear';
}

if (paragraphs[0].className === 'apple') {
  paragraphs[2].innerHTML = 'dog';
}

paragraphs[0].className = 'red apple';

paragraphs[1].style.borderRadius = 0;
