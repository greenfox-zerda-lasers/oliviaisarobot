# create a 300x300 canvas.
# create a square drawing function that takes 1 parameter:
# the square size
# and draws a square of that size to the center of the canvas.
# draw 3 squares with that function.

from tkinter import *

base = Tk()

canvas = Canvas(base, width=300, height=300, bg="white")
canvas.pack()

def draw_square(a):
    canvas.create_rectangle(150-a/2, 150-a/2, 150+a/2, 150+a/2, fill="teal", outline="white", width=10)

draw_square(150)
draw_square(100)
draw_square(50)

base.mainloop()
