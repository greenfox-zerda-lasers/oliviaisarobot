from tkinter import *
from math import *

base = Tk()

size = 600
canvas = Canvas(base, width=size, height=size, bg="white")
canvas.pack()

def draw_hexagon(side, x, y):
    p1p2 = canvas.create_line(x-side/2, y-cos(30*180/pi)*side, x+side/2, y-cos(30*180/pi)*side)
    p2p3 = canvas.create_line(x+side/2, y-cos(30*180/pi)*side, x+side, y)
    p3p4 = canvas.create_line(x+side, y, x+side/2, y+cos(30*180/pi)*side)
    p4p5 = canvas.create_line(x+side/2, y+cos(30*180/pi)*side, x-side/2, y+cos(30*180/pi)*side)
    p4p6 = canvas.create_line(x-side/2, y+cos(30*180/pi)*side, x-side, y)
    p6p1 = canvas.create_line(x-side, y, x-side/2, y-cos(30*180/pi)*side)

def hexa(x, y, scale, n):
    if n <= 0:
        return
    draw_hexagon(scale/3, x, y)

    hexa(x-scale/6/2, y+cos(30*180/pi)*scale/6, scale/2, n-1)
    hexa(x+scale/6, y, scale/2, n-1)
    hexa(x-scale/6/2, y-cos(30*180/pi)*scale/6, scale/2, n-1)

#draw_hexagon(100, 300, 300)
hexa(300, 300, 800, 6)

base.mainloop()
