# reproduce this: [https://github.com/greenfox-velox/velox-syllabus/blob/master/week-04/3-graphics/workshop/r2.png]
# can you make the colors change? make every line a different color.

from tkinter import *

base = Tk()

canvas = Canvas(base, width=300, height=300, bg="white")
canvas.pack()

def draw():
    a = 0
    b = 10
    for n in range(16):
        canvas.create_line(a, 150, 150, 150-b, fill="teal")
        a += 10
        b += 10
    a = 0
    b = 10
    for n in range(16):
        canvas.create_line(a, 150, 150, 150+b, fill="teal")
        a += 10
        b += 10
    a = 0
    b = 10
    for n in range(15):
        canvas.create_line(150, a, 150+b, 150, fill="teal")
        a += 10
        b += 10
    a = 300
    b = 10
    for n in range(16):
        canvas.create_line(a, 150, 150, 150+b, fill="teal")
        a -= 10
        b += 10

draw()

base.mainloop()

# TO BE CHANGED: WHAT'S UP WITH THE COLOR LOOP?
