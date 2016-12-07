'use strict';

function each(arr, func) {
  for (var i = 0, l = arr.length; i < l; i++) {
    func(arr[i]);
  }
}

var newArray = [1, 2, 3, 4]

each(newArray, console.log);

// write a function called each that takes an array and a function as a paramter
// and calls the function with each element of the array as parameter
// so it should call the array 3 times if the array has 3 elements
