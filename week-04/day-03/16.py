# create a 300x300 canvas.
# make it look like a nigth sky:
# - The background should be black
# - The stars can be small squares
# - The stars should have random positions on the canvas
# - The stars should have random color (some shade of grey)

from tkinter import *
from random import randint
from webcolors import rgb_to_hex
base = Tk()

canvas = Canvas(base, width=700, height=700, bg="black")
canvas.pack()

def random_stars(num):
    for a in range(num):
        c = randint(0, 55)
        color = rgb_to_hex([c, c, c])
        x = randint(0, 700)
        y = randint(0, 700)
        canvas.create_rectangle(x, y, x+2, y+2, fill=color)

random_stars(3000)

base.mainloop()

# FIGURE OUT COLOR RANGE
