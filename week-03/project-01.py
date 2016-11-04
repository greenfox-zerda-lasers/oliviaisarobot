# Create a function that takes a string and creates a palindrome from it. It should work like this:
# output = create_palindrome('pear')
# print(output)
# it prints: pearraep

class Palindrome():
    string = []

    def __init__(self, string):
        self.string = string

    def get_string(self):
        return self.string

    def pal_create(self):
        for i in range(len(self.string)-1, -1, -1):
            self.string += self.string[i]
        return self.string

new = Palindrome("olivia")
print(new.get_string())
new2 = Palindrome("gardiner")
print(new2.get_string())
print(new.pal_create())
print(new2.pal_create())
