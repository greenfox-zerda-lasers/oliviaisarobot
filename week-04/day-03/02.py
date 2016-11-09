# create a 300x300 canvas.
# draw a box that has different colored lines on each edge.

from tkinter import *

base = Tk()

canvas = Canvas(base, width=300, height=300)
canvas.pack()

canvas.create_rectangle(100, 100, 200, 200, fill="pink")
canvas.create_line(100, 100, 100, 200, fill="red")
canvas.create_line(100, 200, 200, 200, fill="yellow")
canvas.create_line(200, 100, 200, 200, fill="teal")
canvas.create_line(100, 100, 200, 100, fill="orange")

base.mainloop()
