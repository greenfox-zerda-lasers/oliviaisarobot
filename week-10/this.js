'use strict';

// CASE 1
// function invocation

function cica() {
  console.log(this);
}
cica();
// this = global object in non-strict mode
// undefined

// CASE 2
// method invocation

const kanape = {
  allat: cica
  // integrates the above function called cica
  // allat: function cica() {console.log(this)}
}
kanape.allat();
// this = kanape

// CASE 3
// constructor invocation

var mici = new cica();
// this = newly defined cica object

// CASE 4
// indirect invocation

cica.call('barmi', 'mici');
cica.apply('barmi', ['feri']); // expects an array
// this = parameter that is passed

var mici = cica.bind('barmi'); // if you call the function in the future, this will be bound to the parameter
mici();
