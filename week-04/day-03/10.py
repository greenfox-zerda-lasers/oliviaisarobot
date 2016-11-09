# create a 300x300 canvas.
# create a square drawing function that takes 1 parameter:
# the square size
# and draws a square of that size to the center of the canvas.
# create a loop that draws 20 squares with that function.

from tkinter import *

base = Tk()

canvas = Canvas(base, width=300, height=300, bg="white")
canvas.pack()

def draw_20_square(a):
    x = 1
    while x < 21:
        canvas.create_rectangle(150-a/2, 150-a/2, 150+a/2, 150+a/2, fill="teal", outline="white")
        a -= 10
        x += 1

draw_20_square(200)

base.mainloop()
