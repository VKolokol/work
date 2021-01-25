from tkinter import *


def motion(event):
    s = list(map(float, [event.x - 20, event.y - 20, event.x + 20, event.y + 20]))
    x1 = c.coords(ball)[0]
    y1 = c.coords(ball)[1]

    x2 = round(event.x-20, 2)
    y2 = round(event.y-20, 2)
    try:
        k = round(((y1 - y2) / (x1 - x2)), 2)
    except ZeroDivisionError:
        k = 0
    b = round(y2 - k * x2, 2)
    a = []
    for el1, el2 in zip(s, c.coords(ball)):
        a.append(el1 - el2)
    c.unbind('<Button-1>')
    click(float(x2), float(y2), x1, y1, a, k, b)


def click(x2, y2, x1, y1, a, k, b):

    if round(x2,2) == c.coords(ball)[0] and round(y2,2) == int(c.coords(ball)[1]):
        c.bind('<Button-1>', motion)
    else:
        if int(c.coords(ball)[0]) == int(x2):
            x1 += 0
        else:
            if a[0] < 0:
                x1 = x1 - 1
            if a[0] > 0:
                x1 = x1 + 1
        if int(c.coords(ball)[1]) == int(y2):
            y1 += 0
        else:
            y1 = round(k*x1+b,2)
        c.coords(ball, x1, y1, x1+40, y1+40)
        root.after(2, lambda: click(x2, y2, x1, y1, a, k, b))


root = Tk()

c = Canvas(root, width=300, height=200, bg="white")
c.pack(fill=BOTH, expand=1)
ball = c.create_oval(0, 100, 40, 140, fill='Darkblue')
c.bind('<Button-1>', motion)
root.minsize(width=300, height=200)
root.mainloop()
