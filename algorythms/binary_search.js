// Implement the binary search algorithm as a method, in a programing language of your favor. The method should take a sorted array of numbers and a number. (The array can be any array like container like vector) The method should return true if the array consists the number and false otherwise. The method should have better than linear order of growth based on the input array size.

'use strict';

let search = (sorted, num) => {
  for (let item of sorted) {
    if (item === num) {
      return true
    }
  }
  return false
};

console.log(search([2,3,5,7,9,23,35,55,61,63,64,89], 23));
console.log(search([2,3,5,7,9,23,35,55,61,63,64,89], 21));
