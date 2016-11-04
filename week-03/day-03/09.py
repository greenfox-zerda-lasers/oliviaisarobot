# Create a function that prints a triangle like this:
#   *
#   **
#   ***
#   ****
#   *****
#   ******
# It should take a number as parameter that describes how many lines the triangle has

class Stars():

    def __init__(self):
        lines = ""

    def set_lines(self, lines):
        self.lines = lines
        for i in range(0, lines):
            print("* " * i)
        for i in range(lines, 0, -1):
            print("* " * i)

new = Stars()
new.set_lines(8)
new.set_lines(3)
