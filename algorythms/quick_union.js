// Implement the quick union algorithm as an object. It should take an array length in its constructor. It should have a unite method that takes two indexes of nodes and connects them. It should have a find method that takes two indexes of nodes and returns a boolean if they are in the same group. It shoudl have a getGroups method that returns a list of all groups.

'use strict';

class Union {
  constructor(arrlength) {
    this.length = arrlength;
    this.nodes = [];

    for (let i=0; i < arrlength; i++) {
      this.nodes.push(i);
    }
  }

  unite(id1, id2) {
    if (id1 < this.length && id2 < this.length) {
      this.nodes[id2] = id1;
    } else {
      console.log("Error: index out of range")
    }
  }

  find(id1, id2) {
    if (id1 < this.length && id2 < this.length) {
      if (this.root(id1) === this.root(id2)) {
        console.log(true)
      } else {
        console.log(false)
      }
    } else {
      console.log("Error: index out of range")
    }
  }

  root(ind) {
    while (this.nodes[ind] != ind) {
      ind = this.nodes[ind]
    }
    return ind
  }

  getGroups() {
    // what kind of output is expected???
  }
};

let myUnion = new Union(10);
console.log(myUnion.nodes);
myUnion.unite(6,5);
myUnion.unite(3,9);
myUnion.unite(3,6);
// myUnion.unite(3,10); // error
myUnion.find(5,3); // true
myUnion.find(5,7); // false
myUnion.getGroups();
