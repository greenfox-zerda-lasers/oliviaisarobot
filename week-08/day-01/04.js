// Create a constructor for creating Aircrafts,
// and one for creating Carriers,
// based on the specification in the python exam: https://github.com/greenfox-academy/zerda-exam-python-retake

'use strict';

function Aircraft(type) {
  this.type = type;
  this.ammo = 0;
  this.alldmg = 0;
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

Aircraft.prototype.getStatus = function() {
  console.log('Type ' + this.type + ', Ammo: ' + this.ammo + ', Base damage: ' + this.basedmg + ', All damage: ' + this.alldmg);
}

Aircraft.prototype.fight = function() {
  if (this.ammo === 0) {
    console.log('Out of ammo')
  } else {
    console.log('The aircraft dealt ' + this.ammo * this.basedmg + ' total damage');
    this.alldmg += this.ammo * this.basedmg;
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

function Carrier(ammo) {
  this.ammo = ammo;
  this.hp = 3000;
  this.aircount = 0;
  this.dmg = 3000 - this.hp;
  this.airlist = [];
}

Carrier.prototype.statusReport = function() {
  if (this.hp <= 0) {
    console.log('It\'s dead, Jim :(');
  } else {
    if (this.aircount === 0) {
      console.log('Aircraft count: ' + this.aircount + ', Ammo storage: ' + this.ammo + ', Total damage: ' + this.dmg + ', Health remaining: ' + this.hp);
    } else {
      console.log('Aircraft count: ' + this.aircount + ', Ammo storage: ' + this.ammo + ', Total damage: ' + this.dmg + ', Health remaining: ' + this.hp);
      // console.log('Aircrafts:');
      console.log(this.airlist);
      for (var i = 0; i < this.airlist.length; i++) {
        console.log(this.airlist[i].getStatus());
      }
    }
  }
}

Carrier.prototype.addAircraft = function(name) {
  this.aircount += 1;
  this.airlist.push(name);
}

Carrier.prototype.fill = function() {
  if (this.ammo <= 0) {
    console.log('Out of ammo, unable to fill');
  } else {
    var needed = this.airlist[i].maxammo - this.airlist[i].ammo;
    if (this.ammo <= needed) {
      console.log('Not enough ammo to fill')
    } else {
      for (var i = 0; i < this.airlist.length; i++) {
        this.airlist[i].ammo += needed;
        this.ammo -= needed;
      }
    }
  }
}

Carrier.prototype.fight = function() {
  var totalAmmo = this.airlist.filter(function(aircraft) {
    return aircraft.ammo
  })
  console.log(totalAmmo);
  if (this.ammo === 0) {
    console.log('Out of ammo')
  } else {
    console.log('The aircraft dealt ' + this.ammo * this.basedmg.bind(Aircraft) + ' total damage');
    this.alldmg += this.ammo * this.basedmg.bind(Aircraft);
    this.ammo = 0;
  }
}

// look up BINDNG this!

let acone = new Aircraft('F16');
let actwo = new Aircraft('F35');
acone.getStatus();
acone.fight();
acone.refill(6);
acone.refill(4);
acone.fight();
acone.refill(5);
acone.getStatus();
let carrione = new Carrier(150);
carrione.statusReport();
carrione.addAircraft(acone);
carrione.addAircraft(actwo);
carrione.statusReport();
carrione.fight();
