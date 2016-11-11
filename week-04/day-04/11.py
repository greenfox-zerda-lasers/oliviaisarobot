from tkinter import *

base = Tk()

size = 600
newcanvas = Canvas(base, width=size, height=size, bg="yellow")
newcanvas.pack()

def fractal_square(x, y, scale, n):
    newcanvas.create_rectangle(x, y, x+scale, y+scale)
    if n > 0:
        fractal_square(x, y+scale/3, scale/3, n-1)
        fractal_square(x+(scale*(2/3)), y+scale/3, scale/3, n-1)
        fractal_square(x+scale/3, y, scale/3, n-1)
        fractal_square(x+scale/3, y+(scale*(2/3)), scale/3, n-1)

fractal_square(50, 50, 500, 4)

base.mainloop()
