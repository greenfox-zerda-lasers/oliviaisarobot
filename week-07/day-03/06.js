'use strict';

function isItIn(str, letter) {
   if (str.indexOf(letter)) {
     return false;
   } else {
     return true;
   }
}

console.log(isItIn('apple', 'a'))
console.log(isItIn('apple', 'b'))
// create a function that takes a string and a letter and returns a boolean
// it should return true if the string consits the given letter, false otherwise
