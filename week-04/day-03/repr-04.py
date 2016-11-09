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

def draw_hexagon(size, x, y):
    canvas.create_line(x-size, y, x+size/2, y)
    canvas.create_line(x-size, y, x-(size+size/2), y+size)
    canvas.create_line(x-(size+size/2), y+size, x-size, y+size*2)
    canvas.create_line(x-size, y+size*2, x+size/2, y+size*2)
    canvas.create_line(x+size/2, y+size*2, x+size, y+size)
    canvas.create_line(x+size, y+size, x+size/2, y)

def hexagons(levels):
    x = 150
    y = 0
    for n in range(1,levels+1):
        y += 10
        for i in range(n):
            if i == 0:
                x -= 20
            else:
                x += 40
            draw_hexagon(10, x, y)
        x = 150-n*20

    x = 150-(levels)*20
    y = 0 + (levels)*10
    for m in range(levels-1):
        if m == 0:
            y += 10
        else:
            y += 20
        for i in range(n-1):
            if i == 0:
                x += 20
            else:
                x += 40
            draw_hexagon(10, x, y)
        x = 150-n*20

    x = 150-n*20
    y = 0 + n*10
    for m in range(levels-1):
        y += 20
        for i in range(n):
            if i == 0:
                x += 0
            else:
                x += 40
            draw_hexagon(10, x, y)
        x = 150-n*20

    x = 150-n*20
    y = levels*10 + levels*20 -30
    for n in range(levels+1, 0, -1):
        if n == levels+1:
            x -= 40
        y += 10
        for i in range(n-1, 0, -1):
            x += 40
            draw_hexagon(10, x, y)
        x = 150-n*20

hexagons(4)

base.mainloop()

# FIGURE OUT COLOR RANGE
