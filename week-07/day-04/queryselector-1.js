var king = document.getElementById('b325').innerHTML;

console.log(king);

var conceited = document.getElementsByClassName('b326');

// console.log(conceited[0].innerHTML);
alert(conceited[0].innerHTML);

var businessLamp = document.getElementsByClassName('asteroid big');

for (var i = 0; i < businessLamp.length; i++) {
  console.log(businessLamp[i].innerHTML);
}

var conceitedKing = document.querySelectorAll('div.asteroid');

for (var i = 0; i < conceitedKing.length - 1; i++) {
  alert(conceitedKing[i].innerHTML);
}

var noBusiness = document.querySelectorAll('div.asteroid');

for (var i = 0; i < noBusiness.length; i++) {
  console.log(noBusiness[i].innerHTML);
}

var allBizniss = document.getElementsByTagName('p');

alert(allBizniss[0].innerHTML);
