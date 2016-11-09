# create a 300x300 canvas.
# draw a green 10x10 square to its center.

from tkinter import *

base = Tk()

canvas = Canvas(base, width=300, height=300)
canvas.pack()

canvas.create_rectangle(145, 145, 155, 155, fill="green")

base.mainloop()
