'use strict';

function factorial(a) {
  var output = 1
  for (var x = 1; x <= a; x++) {
    output *= x
  }
  return output
}

console.log(factorial(5))
// create a function that returns it's input factorial
