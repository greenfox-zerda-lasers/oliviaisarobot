from tkinter import *
from math import *

base = Tk()

size = 700
canvas = Canvas(base, width=size, height=size, bg="white")
canvas.pack()

def draw_triangle(side, x, y):
    p1p2 = canvas.create_line(x, y-side/sqrt(3), x+side/2, y+(sqrt(3)/2*side-side/sqrt(3)))
    p2p3 = canvas.create_line(x+side/2, y+(sqrt(3)/2*side-side/sqrt(3)), x-side/2, y+(sqrt(3)/2*side-side/sqrt(3)))
    p3p1 = canvas.create_line(x-side/2, y+(sqrt(3)/2*side-side/sqrt(3)), x, y-side/sqrt(3))

def tri_fractal(side, x, y, n):
    if n <= 0:
        return
    draw_triangle(side, x, y)

    tri_fractal(side/2, x, y-side/sqrt(3)/2, n-1)
    tri_fractal(side/2, x-side/4, y+side/sqrt(3)/4, n-1)
    tri_fractal(side/2, x+side/4, y+side/sqrt(3)/4, n-1)

#draw_triangle(400, 300, 300)
tri_fractal(600, 350, 350, 9)

base.mainloop()
