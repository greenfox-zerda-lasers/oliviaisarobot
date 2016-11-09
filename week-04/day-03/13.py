# create a 300x300 canvas.
# create a line drawing function that takes 2 parameters:
# the x and y coordinates of the line's starting point
# and draws a line from that point to the center of the canvas.
# fill the canvas with lines from the edges, every 20 px, to the center.

from tkinter import *

base = Tk()

canvas = Canvas(base, width=300, height=300, bg="white")
canvas.pack()

def draw_line(x, y):
    for a in range(16):
        canvas.create_line(x, y, 150, 150)
        y += 20
    for a in range(16):
        canvas.create_line(x, y, 150, 150)
        x += 20
    for a in range(16):
        canvas.create_line(x, y, 150, 150)
        y += -20
    for a in range(16):
        canvas.create_line(x, y, 150, 150)
        x += -20

draw_line(0,0)

base.mainloop()
