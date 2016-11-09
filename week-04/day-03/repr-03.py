# create a 300x300 canvas.
# make it look like a nigth sky:
# - The background should be black
# - The stars can be small squares
# - The stars should have random positions on the canvas
# - The stars should have random color (some shade of grey)

from tkinter import *
from random import randint

base = Tk()

canvas = Canvas(base, width=300, height=300, bg="white")
canvas.pack()

def triangles(levels):
    x = 150
    y = 0
    for n in range(1,levels+1):
        y += 20
        x -= 10
        for i in range(n+1):
            if i == 0:
                x -= 0
            elif i == n:
                x = 150-n*10
            else:
                x += 20
            canvas.create_line(x, y, x-10, y+20)
            canvas.create_line(x-10, y+20, x+10, y+20)
            canvas.create_line(x, y, x+10, y+20)

triangles(13)

base.mainloop()

# FIGURE OUT COLOR RANGE
