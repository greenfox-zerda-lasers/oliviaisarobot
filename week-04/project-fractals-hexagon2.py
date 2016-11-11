from tkinter import *
from math import *
from random import *
from webcolors import rgb_to_hex

base = Tk()

size = 600
canvas = Canvas(base, width=size, height=size, bg="black")
canvas.pack()

def draw_hexagon(side, x, y, color):
    p1p2 = canvas.create_line(x, y, x+side, y, fill=color, width=2)
    p2p3 = canvas.create_line(x+side, y, x+side+side/2, y-cos(30*180/pi)*side, fill=color, width=2)
    p3p4 = canvas.create_line(x+side+side/2, y-cos(30*180/pi)*side, x+side, y-cos(30*180/pi)*side*2, fill=color, width=2)
    p4p5 = canvas.create_line(x+side, y-cos(30*180/pi)*side*2, x, y-cos(30*180/pi)*side*2, fill=color, width=2)
    p4p6 = canvas.create_line(x, y-cos(30*180/pi)*side*2, x-side/2, y-cos(30*180/pi)*side, fill=color, width=2)
    p6p1 = canvas.create_line(x-side/2, y-cos(30*180/pi)*side, x, y, fill=color, width=2)

def hexa(x, y, scale, n):
    if n <= 0:
        return
    a = randint(0, 255)
    b = randint(0, 255)
    c = randint(0, 255)
    color = rgb_to_hex([a, b, c])

    draw_hexagon(scale/3, x, y, color)

    hexa(x, y, scale/3, n-1)
    hexa(x, y-scale/3*cos(30*180/pi)*4/3, scale/3, n-1)
    hexa(x+scale/3*(2/3), y, scale/3, n-1)
    hexa(x+scale/3*(2/3), y-scale/3*cos(30*180/pi)*4/3, scale/3, n-1)
    hexa(x-scale/3*(1/3), y-scale/3*(2/3)*cos(30*180/pi), scale/3, n-1)
    hexa(x+scale/3, y-scale/3*(2/3)*cos(30*180/pi), scale/3, n-1)

#draw_hexagon(100, 50, 50)
hexa(150, 100, 700, 4)

base.mainloop()
