# Create a `Stack` class that stores elements
# It should have a `size` method that returns number of elements it has
# It should have a `push` method that adds an element to the stack
# It should have a `pop` method that returns the last element form the stack and also deletes it from it

# please don`t use the built in methods

class Stack():

    def __init__(self):
        self.elements = []

    def size(self):
        return len(self.elements)

    def push(self, num):
        self.num = num
        self.elements.append(self.num)
        return self.elements

    def pop(self):
        self.elements = self.elements[0:len(self.elements)-1]
        return self.elements

    def get_elements(self):
        print(str(self.elements))

newstack = Stack()
print(newstack.size())
newstack.push(20)
newstack.push(11)
newstack.push(7)
print(newstack.size())
newstack.get_elements()
newstack.pop()
print(newstack.size())
newstack.get_elements()
