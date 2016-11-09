# create a 300x300 canvas.
# make it look like a nigth sky:
# - The background should be black
# - The stars can be small squares
# - The stars should have random positions on the canvas
# - The stars should have random color (some shade of grey)

from tkinter import *
from random import randint
from colour import rgb2hex

base = Tk()

canvas = Canvas(base, width=300, height=300, bg="black")
canvas.pack()

def random_stars(num):
    for a in range(num):
        c = randint(1, 9)
        color = "#" + str(c) + str(c) + str(c)
        x = randint(0, 300)
        y = randint(0, 300)
        canvas.create_rectangle(x, y, x+2, y+2, fill=color)

random_stars(500)

base.mainloop()

# FIGURE OUT COLOR RANGE
