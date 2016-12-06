'use strict';

var names = ['Zakarias', 'Hans', 'Otto', 'Ole'];

function shortest(array) {
  var output = ''
  for (var x = 0; x < array.length; x++) {
    if (x === 0) {
      output = array[x];
    } else if (x > 0 && array[x].length < output.length) {
      output = array[x];
    } else {
      continue
    }
  }
  return output
}

console.log(shortest(names))
// create a function that returns the shortest string
// from an array
