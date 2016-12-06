'use sttict';

var numbers = [7, 5, 8, -1, 2];

function min(array) {
  var output = 0
  for (var x = 0; x < array.length; x++) {
    if (x === 0) {
      output = array[x];
    } else if (x > 0 && array[x] < output) {
      output = array[x];
    } else {
      continue
    }
  }
  return output
}

console.log(min(numbers))
// Write a function that returns the minimal element
// in an array (your own min function)
