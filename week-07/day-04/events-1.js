var partyButton = document.querySelector('button');
var partyBg = document.querySelector('div');

var clicked = false;

function startTheParty() {
  if (clicked) {
    partyBg.className = '';
    clicked = false;
  } else {
    partyBg.className = 'party';
    clicked = true;
  }
}

partyButton.addEventListener('click', startTheParty)
