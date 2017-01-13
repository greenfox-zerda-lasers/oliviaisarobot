// set up a setInterval loop with 1.5 second delays
// - log the mouse coordinates on each call

'use strict';

window.addEventListener('mousemove', mousepos);
var posX, posY

function mousepos(e) {
  posX = e.clientX;
  posY = e.clientY;
}

function log() {
  console.log("mouse location:", posX, posY);
}

setInterval(log, 1500);
