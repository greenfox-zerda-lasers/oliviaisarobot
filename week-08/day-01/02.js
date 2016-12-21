'use strict';

function Rectangle(a, b) {
  this.a = a,
  this.b = b
}

Rectangle.prototype.getArea = function() {
  console.log(this.a * this.b)
}

Rectangle.prototype.getCircumference = function() {
  console.log(this.a * 2 + this.b * 2)
}

let newRectangle = new Rectangle(15, 20);
newRectangle.getArea();
newRectangle.getCircumference();

// Create a constructor for creating Rectangles.
// it should take two parameters: the sides of the rectangle
// Every rectangle should have a method called getArea() that returns its area
// Every rectangle should have a method called getCircumference() that returns its circumference
