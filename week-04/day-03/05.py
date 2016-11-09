# create a 300x300 canvas.
# create a line drawing function that takes 2 parameters:
# the x and y coordinates of the line's starting point
# and draws a 50 long horizontal line from that point.
# draw 3 lines with that function.

from tkinter import *

base = Tk()

canvas = Canvas(base, width=300, height=300)
canvas.pack()

def draw_line(x, y):
    canvas.create_line(x, y, x+50, y, fill="green")

draw_line(30, 50)
draw_line(55, 10)
draw_line(0, 100)

base.mainloop()
