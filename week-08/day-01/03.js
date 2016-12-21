'use strict';

function Rocket(consumption) {
  this.consumption = consumption;
  this.level = 0;
  this.launches = 0
}

Rocket.prototype.fill = function(amount) {
  this.level += amount;
  console.log('Rocket fuel level is: ' + this.level)
}

Rocket.prototype.launch = function() {
  if (this.level >= this.consumption) {
    this.launches += 1;
    console.log('Rocket launched')
  } else {
    console.log('Not enough fuel to launch')
  }
}

let testRocket = new Rocket(20);
testRocket.launch();
testRocket.fill(30);
testRocket.launch();

// Create a constructor for creating Rockets.
// it should take one parameter: the consumption of the rocket
// (amount of fuel needed for launch)
// Every rocket should have a method called fill(amount) that fills the tank of
// the rocket with the amount of fuel given as a parameter
// Every rocket should have a method called launch() that launches the rocket
// if it has enough fuel (more than its consumption)
