# create a 300x300 canvas.
# create a function that takes 1 parameter:
# a list of [x, y] points
# and connects them with green lines.
# connect these to get a box: [[10, 10], [290,  10], [290, 290], [10, 290]]
# connect these: [[50, 100], [70, 70], [80, 90], [90, 90], [100, 70],
# [120, 100], [85, 130], [50, 100]]

from tkinter import *

base = Tk()

canvas = Canvas(base, width=300, height=300, bg="white")
canvas.pack()

def connect(dots):
    for n in range(-1, len(dots)-1):
        canvas.create_line(dots[n][0], dots[n][1], dots[n+1][0], dots[n+1][1], fill="green")

list1 = [[10, 10], [290,  10], [290, 290], [10, 290]]
list2 = [[50, 100], [70, 70], [80, 90], [90, 90], [100, 70], [120, 100], [85, 130], [50, 100]]

#connect(list1)
connect(list2)

base.mainloop()
