# create a 300x300 canvas.
# fill it with a checkerboard pattern.

from tkinter import *

base = Tk()

canvas = Canvas(base, width=300, height=300, bg="white")
canvas.pack()

def checked():
    x = 0
    y = 0
    a = 1
    while a < 1:
        if a%2 == 0:
            canvas.create_rectangle(x, y, x+30, y+30, fill="white")
        else:
            canvas.create_rectangle(x, y, x+30, y+30, fill="black")
        a += 1
        x += 30
    x = 0
    y = 30
    while 10 < a < 21:
        if a%2 == 1:
            canvas.create_rectangle(x, y, x+30, y+30, fill="white")
        else:
            canvas.create_rectangle(x, y, x+30, y+30, fill="black")
        a += 1
        x += 30
    x = 0
    y = 60
    while 20 < a < 31:
        if a%2 == 0:
            canvas.create_rectangle(x, y, x+30, y+30, fill="white")
        else:
            canvas.create_rectangle(x, y, x+30, y+30, fill="black")
        a += 1
        x += 30
    x = 0
    y = 90
    while 30 < a < 41:
        if a%2 == 1:
            canvas.create_rectangle(x, y, x+30, y+30, fill="white")
        else:
            canvas.create_rectangle(x, y, x+30, y+30, fill="black")
        a += 1
        x += 30
    x = 0
    y = 120
    while 40 < a < 51:
        if a%2 == 0:
            canvas.create_rectangle(x, y, x+30, y+30, fill="white")
        else:
            canvas.create_rectangle(x, y, x+30, y+30, fill="black")
        a += 1
        x += 30
    x = 0
    y = 150
    while 50 < a < 61:
        if a%2 == 1:
            canvas.create_rectangle(x, y, x+30, y+30, fill="white")
        else:
            canvas.create_rectangle(x, y, x+30, y+30, fill="black")
        a += 1
        x += 30
    x = 0
    y = 180
    while 60 < a < 71:
        if a%2 == 0:
            canvas.create_rectangle(x, y, x+30, y+30, fill="white")
        else:
            canvas.create_rectangle(x, y, x+30, y+30, fill="black")
        a += 1
        x += 30
    x = 0
    y = 210
    while 70 < a < 81:
        if a%2 == 1:
            canvas.create_rectangle(x, y, x+30, y+30, fill="white")
        else:
            canvas.create_rectangle(x, y, x+30, y+30, fill="black")
        a += 1
        x += 30
    x = 0
    y = 240
    while 80 < a < 91:
        if a%2 == 0:
            canvas.create_rectangle(x, y, x+30, y+30, fill="white")
        else:
            canvas.create_rectangle(x, y, x+30, y+30, fill="black")
        a += 1
        x += 30
    x = 0
    y = 270
    while 90 < a < 101:
        if a%2 == 1:
            canvas.create_rectangle(x, y, x+30, y+30, fill="white")
        else:
            canvas.create_rectangle(x, y, x+30, y+30, fill="black")
        a += 1
        x += 30

checked()

base.mainloop()
