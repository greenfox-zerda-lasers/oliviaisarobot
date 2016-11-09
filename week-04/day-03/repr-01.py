from tkinter import *

base = Tk()

canvas = Canvas(base, width=300, height=300, bg="white")
canvas.pack()

def draw_square_times(x, y, times):
    t = 1
    while t < times+1:
        canvas.create_rectangle(x, y, x+15, y+15, fill="teal")
        t += 1
        x += 15
        y += 15

draw_square_times(15, 15, 15)

base.mainloop()
