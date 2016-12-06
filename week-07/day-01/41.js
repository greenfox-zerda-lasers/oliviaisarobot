'use strict';

var numbers = [4, 5, 6, 7, 8, 9, 10]

function sum(array) {
  var output = 0
  for (var x = 0; x < array.length; x++) {
    output += array[x];
  }
  return output
}

console.log(sum(numbers))
// write your own sum function
