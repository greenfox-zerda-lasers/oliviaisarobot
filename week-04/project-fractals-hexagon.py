from tkinter import *
from math import *

base = Tk()

size = 800
canvas = Canvas(base, width=size, height=size, bg="teal")
canvas.pack()

def draw_hexagon(side, x, y):
    p1p2 = canvas.create_line(x, y, x+side, y, fill="white")
    p2p3 = canvas.create_line(x+side, y, x+side+side/2, y-cos(30*180/pi)*side, fill="white")
    p3p4 = canvas.create_line(x+side+side/2, y-cos(30*180/pi)*side, x+side, y-cos(30*180/pi)*side*2, fill="white")
    p4p5 = canvas.create_line(x+side, y-cos(30*180/pi)*side*2, x, y-cos(30*180/pi)*side*2, fill="white")
    p4p6 = canvas.create_line(x, y-cos(30*180/pi)*side*2, x-side/2, y-cos(30*180/pi)*side, fill="white")
    p6p1 = canvas.create_line(x-side/2, y-cos(30*180/pi)*side, x, y, fill="white")

def hexa(x, y, scale, n):
    if n <= 0:
        return
    draw_hexagon(scale/3, x, y)

    hexa(x, y, scale/3, n-1)
    hexa(x, y-scale/3*cos(30*180/pi)*4/3, scale/3, n-1)
    hexa(x+scale/3*(2/3), y, scale/3, n-1)
    hexa(x+scale/3*(2/3), y-scale/3*cos(30*180/pi)*4/3, scale/3, n-1)
    hexa(x-scale/3*(1/3), y-scale/3*(2/3)*cos(30*180/pi), scale/3, n-1)
    hexa(x+scale/3, y-scale/3*(2/3)*cos(30*180/pi), scale/3, n-1)

#draw_hexagon(100, 50, 50)
hexa(200, 100, 800, 5)

base.mainloop()
