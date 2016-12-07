'use strict';

function letterCount(str) {
  var newDict = {};
  str.split('').forEach(function(e) {
    if (e in newDict) {
      newDict[e] += 1;
    } else {
      newDict[e] = 1;
    }
  })
  console.log(newDict);
}

letterCount('apple');

// create a function that takes a string and counts its letters
// it should return an object thats keys are the letters and the values are
// the counts.
// example: "apple" -> {a: 1, p: 2, l: 1, e: 1}
