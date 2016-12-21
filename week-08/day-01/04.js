'use strict';

function Aircraft(type) {
  this.type = type;
  this.ammo = 0;
  if (type === 'F16') {
    this.maxammo = 8;
    this.basedmg = 30;
  } else if (type === 'F35') {
    this.maxammo = 12;
    this.basedmg = 50;
  } else {
    console.log('This is not a valid aircraft type');
  }
}

Aircraft.prototype.fight = function() {
  if (this.ammo === 0) {
    console.log('Out of ammo')
  } else {
    console.log('The aircraft dealt ' + this.ammo * this.basedmg + ' total damage');
    this.ammo = 0;
  }
}

Aircraft.prototype.refill = function(amount) {
  if (this.ammo + amount <= this.maxammo) {
    this.ammo += amount;
    console.log('Ammo refilled, current ammo is ' + this.ammo);
  } else if (this.ammo + amount > this.maxammo) {
    var excess = (this.ammo + amount) - this.maxammo;
    console.log('Ammo refilled, excess of ' + excess + ' is returned');
    this.ammo = this.maxammo;
  }
}

// function Carrier() {
//
// }

let acone = new Aircraft('F16');
let actwo = new Aircraft('F35');
acone.fight();
acone.refill(6);
acone.refill(4);
acone.fight();

// Create a constructor for creating Aircrafts,
// and one for creating Carriers,
// based on the specification in the python exam: https://github.com/greenfox-academy/zerda-exam-python-retake
