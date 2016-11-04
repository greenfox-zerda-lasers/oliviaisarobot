# Create a function that prints a diamond like this:
#       *
#      ***
#     *****
#    *******
#   *********
#  ***********
#   *********
#    *******
#     *****
#      ***
#       *
#
# It should take a number as parameter that describes how many lines the diamond has

class Xmastree():

    def __init__(self):
        lines = ""

    def set_lines(self, lines):
        self.lines = lines
        x = 1
        y = lines//2
        if lines%2 is 1:
            for i in range(lines, lines//2+1, -1):
                print(" " * y + "* " * x)
                x += 1
                y -= 1
            for i in range(lines//2, -1, -1):
                print(" " * y + "* " * x)
                x -= 1
                y += 1
        else:
            for i in range(lines, lines//2, -1):
                print(" " * y + "* " * x)
                x += 1
                y -= 1
            x -= 1
            y += 1
            for i in range(lines//2, 0, -1):
                print(" " * y + "* " * x)
                x -= 1
                y += 1


new = Xmastree()
new.set_lines(12)
