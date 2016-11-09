# create a 300x300 black canvas.
# draw a red horizontal line to its middle.
# draw a green vertical line to its middle.

from tkinter import *

base = Tk()

canvas = Canvas(base, width=300, height=300, bg="black")
canvas.pack()

canvas.create_line(0, 150, 300, 150, fill="red")
canvas.create_line(150, 0, 150, 300, fill="green")

base.mainloop()
