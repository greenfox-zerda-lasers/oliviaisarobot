# create a 300x300 canvas.
# fill it with four different size and color rectangles.

from tkinter import *

base = Tk()

canvas = Canvas(base, width=300, height=300)
canvas.pack()

canvas.create_rectangle(75, 75, 250, 250, fill="blue")
canvas.create_rectangle(50, 50, 190, 190, fill="aqua")
canvas.create_rectangle(30, 30, 110, 110, fill="teal")
canvas.create_rectangle(15, 15, 50, 50, fill="green")

base.mainloop()
