'use strict';

var numbers = [3, 4, 5, 6, 7];

function onlyEven(array) {
  var output = []
  for (var x = 0; x < array.length; x++) {
    if (x % 2 === 0) {
      output.push(x)
    } else {
      continue
    }
  }
  return output
}

console.log(onlyEven(numbers))
// write a function that filters the odd numbers
// from an array and returns a new array consisting
// only the evens
