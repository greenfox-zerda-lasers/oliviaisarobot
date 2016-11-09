# create a 300x300 canvas.
# draw its diagonals in green.

from tkinter import *

base = Tk()

canvas = Canvas(base, width=300, height=300)
canvas.pack()

canvas.create_line(0, 0, 300, 300, fill="green")
canvas.create_line(0, 300, 300, 0, fill="green")

base.mainloop()
