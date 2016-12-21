'use strict';

function Animal(sound) {
  this.sound = sound;
}

Animal.prototype.say = function() {
  console.log(this.sound);
}

let dog = new Animal('woof');
dog.say();

let cat = new Animal('meow');
cat.say();

// Create a constructor for creating Animals.
// it should take one parameter: what the animal says
// Every animal should have a method called say() that prints what the animal says
