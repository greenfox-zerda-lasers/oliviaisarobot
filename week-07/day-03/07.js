'use strict';

var numbers = [2, 5, 11, 29];

function isPrime(number) {
  if (number > 1) {
    for (var i = 2; i < number; i++) {
      if (number % i === 0) {
        return false;
      }
    }
  }
  return true;
}

function allPrime(arr) {
  console.log(arr.every(isPrime));
}

allPrime(numbers);

// create a function that takes an array of numbers and returns a boolean
// it should return true if all the elements are prime, false otherwise
