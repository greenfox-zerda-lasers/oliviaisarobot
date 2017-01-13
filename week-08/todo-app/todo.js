'use strict';

var Todo = function(){
  var addButton = document.querySelector('#add-button');
  var allTodos = document.querySelector('#todo-list');
  // var ajax = new Ajax();
  var todoList = [];

  function render() {

  };

  function newTodo() {
    var name = document.querySelector('#new-item');
    var item = document.createElement('div');

    // if (name.value = "") {
    //   alert("Please name your todo!")
    // } else {
    // };
    item.innerHTML = name.value;
    item.className = 'todo-item';

    createButtons(item);

    allTodos.appendChild(item);

    // ajax post to database
  };

  function createButtons(parent) {
    var delButton = document.createElement('span');
    var check = document.createElement('span');

    delButton.className = 'del-button';
    check.className = 'check';

    parent.appendChild(delButton);
    parent.appendChild(check);

    delButton.addEventListener('click', deleteTodo);
    check.addEventListener('click', function(){
      this.style.backgroundImage = 'url("images/check.svg")';
      this.style.opacity = 1;
    });
  };

  function deleteTodo() {
    console.log('deleted');

    // ajax request to delete from database
  };

  return {
    init:  function(){
      addButton.addEventListener('click', newTodo);

      window.addEventListener('keydown', function(event){
        if (event.keyCode === 13) {
          newTodo();
        }
      })

      // ajax request for items stored in database
    }
  }
}();
