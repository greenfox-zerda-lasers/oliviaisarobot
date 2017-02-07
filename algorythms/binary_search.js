// Implement the binary search algorithm as a method, in a programing language of your favor. The method should take a sorted array of numbers and a number. (The array can be any array like container like vector) The method should return true if the array consists the number and false otherwise. The method should have better than linear order of growth based on the input array size.

'use strict';

let linearSearch = (sorted, num) => {
  for (let item of sorted) {
    if (item === num) {
      return true
    }
  }
  return false
};

class binarySearch {
  constructor (sorted, num) {
    this.sorted = sorted;
    this.num = num;

    this.start = 0;
    this.end = this.sorted.length - 1;
  }

  find() {
    while (this.start < this.end) {
      let mid = Math.floor((this.start + this.end)/2);
      if (this.sorted[mid] < this.num) {
        this.start = mid + 1;
        this.find();
      } else if (this.sorted[mid] > this.num) {
        this.end = mid - 1;
        this.find();
      } else if (this.sorted[mid] === this.num) {
        return true
      }
    }
    return false
  }
}

// console.log(linearSearch([2,3,5,7,9,23,35,55,61,63,64,89], 23)); // 0.213s
// console.log(linearSearch([2,3,5,7,9,23,35,55,61,63,64,89], 21)); // 0.264s

let binary = new binarySearch([2,3,5,7,9,23,35,55,61,63,64,89], 23);
console.log(binary.find()); // 0.178s
// let binary2 = new binarySearch([2,3,5,7,9,23,35,55,61,63,64,89], 21);
// console.log(binary2.find()); // 0.259s
