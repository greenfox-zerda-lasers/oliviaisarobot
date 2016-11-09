# create a 300x300 canvas.
# create a square drawing function that takes 2 parameters:
# the square size, and the fill color,
# and draws a square of that size and color to the center of the canvas.
# create a loop that fills the canvas with rainbow colored squares.

from tkinter import *

base = Tk()

canvas = Canvas(base, width=300, height=300, bg="white")
canvas.pack()

def draw_color_square(a, r, g, b):
    for n in range(10):
        canvas.create_rectangle(150-a/2, 150-a/2, 150+a/2, 150+a/2, fill=color)
        a -= 10
        color =

draw_color_square(200, "orange")

base.mainloop()

# TO BE FIXED: WHAT'S UP WITH THE COLOR LOOP?
