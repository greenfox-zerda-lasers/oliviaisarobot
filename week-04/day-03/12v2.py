# create a 300x300 canvas.
# fill it with a checkerboard pattern.

from tkinter import *

base = Tk()

canvas = Canvas(base, width=300, height=300, bg="white")
canvas.pack()

def checked():
    x = 0
    y = 0
    for a in range(5):
        for a in range(5):
            canvas.create_rectangle(x, y, x+30, y+30, fill="black")
            canvas.create_rectangle(x+30, y, x+30, y+30, fill="white")
            canvas.create_rectangle(x, y+30, x+60, y+60, fill="white")
            canvas.create_rectangle(x+30, y+30, x+60, y+60, fill="black")
            x += 60
        y += 60
        x = 0

checked()

base.mainloop()
