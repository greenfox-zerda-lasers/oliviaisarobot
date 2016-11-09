# reproduce this: [https://github.com/greenfox-velox/velox-syllabus/blob/master/week-04/3-graphics/workshop/r1.png]
# divide the canvas into 4 parts and repeat the pattern.

from tkinter import *

base = Tk()

canvas = Canvas(base, width=300, height=300, bg="white")
canvas.pack()

def draw():
    a = 0
    b = 0
    for n in range(20):
        canvas.create_line(0, a, b, 300, fill="teal")
        a += 15
        b += 15
    a = 0
    b = 0
    for n in range(20):
        canvas.create_line(300, a, b, 0, fill="purple")
        a += 15
        b += 15

draw()

base.mainloop()
