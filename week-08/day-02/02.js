// create a function that starts a setTimeout with a 3 second delay.
// - create a button with an event listener that can cancel the setTimeout

'use strict';

function selfDestruct() {
  alert('You are dead');
}

var timer = setTimeout(selfDestruct, 3000);

function stop() {
  clearTimeout(timer);
  alert('Timer stopped!')
}

var myButton = document.getElementById('stopbutton');

myButton.addEventListener('click', stop);
