import tkinter as tk
from PIL import Image, ImageTk
from tkinter import filedialog as fd


class Contact:
    def __init__(self, name, var_):
        self.img = ''
        self.resize = ''
        tk.Radiobutton(master=f1, text=name, variable=var, value=var_, indicatoron=0, width=15, height=5,
                       command=lambda i=name: self.number(i)).pack(side=tk.BOTTOM)

    def number(self, name):

        root.update_idletasks()
        self.img = Image.open(contactImg.get(name))
        self.img = self.img.resize((150, 160), Image.ANTIALIAS)
        self.resize = ImageTk.PhotoImage(self.img)
        labImg.configure(image=self.resize, width=150, height=160)
        change.configure(text='Изменить фото', fg='blue', font=('bold', 10))
        change.bind('<Button-1>', lambda event, n=name: self.change_img(event, n))
        lab['text'] = contact.get(name)

    def change_img(self, event, name):

        file_name = fd.askopenfilename(filetypes=(("JPG", "*.jpg"), ("PNG", "*.png"), ('GIF', '*.gif')))
        self.img = Image.open(file_name)
        self.img = self.img.resize((150, 160), Image.ANTIALIAS)
        self.resize = ImageTk.PhotoImage(self.img)
        contactImg[name] = file_name
        labImg.configure(image=self.resize)


root = tk.Tk()
root.geometry('450x265')
root.resizable(0, 0)

f1 = tk.Frame(master=root, width=20, height=60)
f1.pack(side=tk.LEFT, pady=5, padx=4)
f2 = tk.Frame(master=root, width=40, height=60)
f2.pack(side=tk.RIGHT)
lab = tk.Label(master=f2, text='Contact list', width=40, height=2)
labImg = tk.Label(master=f2, image=None, width=40, height=10)
change = tk.Label(master=f2, text=None, width=40, height=2)
labImg.pack(side=tk.TOP, pady=10)
lab.pack(side=tk.BOTTOM)
change.pack(side=tk.BOTTOM)

contact = {'Саша': '+6573920', 'Маша': '+8376423847', 'Марина': '+392875873'}
contactImg = {'Саша': 'Sasha.png', 'Маша': 'Masha.png', 'Марина': 'Marina.png'}

var = tk.IntVar()
var.set(0)

for ind, el in enumerate(contact.keys()):
    Contact(el, ind)

tk.mainloop()
