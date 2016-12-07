'use strict';

var student = {

  grades: [],
  addGrade: function(grade) {
    if (grade >= 1 && grade <= 5) {
      this.grades.push(grade);
    }
  },
  getAverage: function() {
    var sum = this.grades.reduce(function(a, b) {
      return a + b;
    }, 0);
    console.log(sum / this.grades.length);
  }
}

student.addGrade(4);
student.addGrade(5);
student.addGrade(4);
student.addGrade(5);
student.getAverage();

// create a student object
// that has a method `addgrade`, that takes a grade from 1 to 5
// an other method `getAverage`, that returns the average of the grades
