# create a function that takes a list and returns a new list with all the elements doubled

class Stuff():

    def __init__(self, *item):
        self.elements = []
        for a in item:
            self.elements.append(a)

    def double_elements(self):
        doubled = []
        for i in range(0, len(self.elements)):
            doubled.append(self.elements[i]*2)
        return doubled

list = Stuff(3, 5, 9, 6, 2)
print(list.double_elements())
list1 = Stuff(5, 34, 9, 21)
print(list1.double_elements())
