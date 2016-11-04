# Create a function that prints a triangle like this:
#       *
#      ***
#     *****
#    *******
#   *********
#  ***********
#
# It should take a number as parameter that describes how many lines the triangle has

class Xmastree():

    def __init__(self):
        lines = ""

    def set_lines(self, lines):
        self.lines = lines
        x = 1
        y = lines
        for i in range(lines, 0, -1):
            print(" " * y + "* " * x)
            x += 1
            y -= 1


new = Xmastree()
new.set_lines(13)
