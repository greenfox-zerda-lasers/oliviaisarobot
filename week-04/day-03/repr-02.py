from tkinter import *

base = Tk()

canvas = Canvas(base, width=300, height=300, bg="white")
canvas.pack()

def draw_square_times(x, y, times):
    t = 1
    while t < times+1:
        canvas.create_rectangle(x, y, x+x/2, y+y/2, fill="teal")
        t += 1
        x += x/2
        y += y/2

draw_square_times(5, 5, 10)

base.mainloop()
