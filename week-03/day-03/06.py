# create a function that takes a list and returns a new list that is reversed

class List():

    def __init__(self, *args):
        self.elements = []
        for a in args:
            self.elements.append(a)

    def get_list(self):
        return self.elements

    def reverse(self):
        revlist = []
        for i in range(len(self.elements)-1, -1, -1):
            revlist.append(self.elements[i])
        return revlist

oldlist = [3, 5, 7, 8, 9]


mylist1 = List(3, 6, 2, 9, 11)
print(mylist1.get_list())
print(mylist1.reverse())
mylist3 = List(15, 47, 4, 678, 2)
mylist2 = List(oldlist)
print(mylist2.get_list())
