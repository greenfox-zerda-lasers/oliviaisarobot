'use strict';

var Stack = {
  elements: [1, 2, 3, 4],
  size: function() {
    var counter = 0
    for (var i = 0; i < this.elements.length; i++) {
      counter++;
    }
    console.log('There are ' + counter + ' elements.');
  },
  push: function(element) {
    this.elements[this.elements.length] = element;
  },
  pop: function() {
    var temp = this.elements[this.elements.length - 1];
    this.elements = this.elements[0, this.elements.length - 2];
    console.log(temp + ' was deleted from the elements.')
  }
}

Stack.size();
Stack.push(5);
Stack.pop();

// Create a `Stack` constructor that stores elements
// It should have a `size` method that returns number of elements it has
// It should have a `push` method that adds an element to the stack
// It should have a `pop` method that returns the last element form the stack and also deletes it from it

// please don`t use the built in methods
