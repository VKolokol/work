from tkinter import *
import random


def change(event):
    root.update_idletasks()
    w = root.winfo_width()
    h = root.winfo_height()
    wid = random.randint(0, w-142)
    hei = random.randint(0, h-142)
    but.place_forget()
    but.place(x=wid, y=hei, width=142, height=142)


def update(ind):

    frame = img[ind]
    ind += 1
    if ind == frameCnt:
        ind = 0
    but.configure(image=frame)
    root.after(100, update, ind)


root = Tk()
root.geometry('400x400')


frameCnt = 12
img = [PhotoImage(file='gif1.gif', format=f'gif -index {i}') for i in range(frameCnt)]
but = Button(master=root)
but.bind('<Button-1>', change)
but.place(relx=0.32,rely=0.25, width=142, height=142)
root.after(0, update, 0)
mainloop()