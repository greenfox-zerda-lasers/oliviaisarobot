from tkinter import *
from random import randint
from webcolors import rgb_to_hex
import math

base = Tk()

w = 900
h = 700
canvas = Canvas(base, width=w, height=h, bg="black")
canvas.pack()

def drawFractalTree(canvas, x1, y1, angle, length, n, c):
    if n == 0:
        return drawFractalTree(canvas, x1, y1, angle, length, n + 1, c)
    elif length:
    #    a = randint(0, 255)
    #    b = randint(0, 255)
        c -= 20
        color = rgb_to_hex([c, c, c])
        x2 = x1 + int(math.cos(math.radians(angle)) * length * 10.0)
        y2 = y1 + int(math.sin(math.radians(angle)) * length * 10.0)
        canvas.create_line(x1, y1, x2, y2, fill=color, width=n)
        # recursive calls
        drawFractalTree(canvas, x2, y2, angle - 20, length - 1, n - 1, c)
        drawFractalTree(canvas, x2, y2, angle + 20, length - 1, n - 1, c)

# starting coordinates (x, y)
x = w/2
y = h - 10
# starting angle
angle = -90
# experiment with length
length = 11
#experiment with line width
n = 8
#starting color
c = 255

canvas.create_line(x+w/4, y+h, x+w*3/4, y+h, fill="white", width=8)
drawFractalTree(canvas, x, y, angle, length, n, c)


base.mainloop()
