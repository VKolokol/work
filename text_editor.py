from tkinter import *
from tkinter import messagebox as mb
from tkinter import filedialog as fd
import os


def name(filename):
    full_name = os.path.basename(filename)
    file = os.path.splitext(full_name)[0]
    root.title('Редактор - {}'.format(file))


def insert_text():
    global file_name
    if text.get('0.0', END) != '\n':
        file = mb.askyesno('Редактор', f'Вы хотите сохранить изменения в файле "{file_name}"?')
        if file == YES:
            save()
    try:
        file_name = fd.askopenfilename(filetypes=(("TXT files", "*.txt"), ('HTML', '*.html')))
        text.delete('0.0', END)
        f = open(file_name, encoding='utf-8')
        name(file_name)
        file = f.read()
        text.insert(1.0, file)
        f.close()
    except FileNotFoundError:
        mb.showwarning('Внимание!', 'Файл не загружен!')


def extract_text():
    try:
        filename = fd.asksaveasfilename(
            filetypes=([("TXT files", ".txt"), ("HTML files", "*.html;*.htm"), ("All files", "*.*")]),
            defaultextension='.txt')
        f = open(filename, 'w')
        file = text.get(1.0, END)
        name(filename)
        f.write(file)
        f.close()
    except FileNotFoundError:
        mb.showwarning('Внимание!', 'Файл не сохранен!')


def delete():
    clear = mb.askyesno('Внимание!', 'Вы действительно хотите удалить содержимое файла?')
    if clear:
        text.delete('0.0', END)


def popup(event):
    menu.post(event.x_root, event.y_root)


def destroy():
    if text.get('0.0', END) == '\n':
        root.destroy()
    else:
        d = mb.askyesnocancel('Редактор', f'Вы хотите сохранить изменения в файле "{file_name}"?')
        if d == YES:
            save()
            root.destroy()
        if d == NO:
            root.destroy()


def save():
    with open(file_name, 'w', encoding='utf-8') as f:
        f.write(text.get('0.0', END))
        f.close()
        name(file_name)


def increase():
    global s
    s += 1
    text['font'] = ("Arial", s)


def reduce():
    global s
    s -= 1
    text['font'] = ("Arial", s)


def select():
    t = text.get('sel.first', 'sel.last')
    root.clipboard_append(t)


def paste():
    p = root.clipboard_get()
    text.insert(INSERT, p)


def del_text():
    text.delete('sel.first', 'sel.last')


def cut():
    t = text.get('sel.first', 'sel.last')
    root.clipboard_append(t)
    del_text()


def replace(event):
    d = Toplevel(master=root, width=20)
    d.title('Заменить')
    d.resizable(0, 0)
    d.geometry('190x75')
    e1 = Entry(master=d)
    e2 = Entry(master=d)
    Label(master=d, text='Что:').grid(row=0, column=1)
    Label(master=d, text='Чем:').grid(row=1, column=1)
    e1.grid(row=0, column=2)
    e2.grid(row=1, column=2)
    Button(master=d, text="Заменить",
           command=lambda:
           text.replace('1.0', END, text.get('1.0', END).replace(e1.get(), e2.get()))) \
        .grid(row=3, column=2, sticky=S, pady=3)


def undo(event):
    try:
        text.edit_undo()
    except TypeError:
        pass


def redo(event):
    try:
        text.edit_redo()
    except TypeError:
        pass


s = 10

root = Tk()
root.geometry('600x600')
root.resizable(1, 1)
file_name = r'C:\Users\Vlad\Desktop\New_file.txt'
root.title('Редактор')
root.protocol("WM_DELETE_WINDOW", destroy)

mainmenu = Menu(root)
root.config(menu=mainmenu)
filemenu = Menu(mainmenu, tearoff=0)
file_font = Menu(mainmenu, tearoff=0)
file_edit = Menu(mainmenu, tearoff=0)
menu = Menu(tearoff=0)

text = Text(master=root, width=50, height=50, font=("Arial", s), undo=True)
text.focus_set()
text.place(relwidth=1, relheight=1)

filemenu.add_command(label='Открыть', command=insert_text)
filemenu.add_command(label='Сохранить как', command=extract_text)
filemenu.add_separator()
filemenu.add_command(label='Выход', command=destroy)

file_font.add_command(label='Увеличить', command=increase)
file_font.add_command(label='Уменьшить', command=reduce)

file_edit.add_command(label='Отмена', command=lambda event='': undo(event))
file_edit.add_command(label='Вернуть', command=lambda event='': redo(event))
file_edit.add_separator()
file_edit.add_command(label='Заменить', command=lambda event='': replace(event))
file_edit.add_command(label='Отчисть', command=delete)
file_edit.add_command(label='Копировать', command=select)
file_edit.add_command(label='Вставить', command=paste)
file_edit.add_command(label='Вырезать', command=cut)
file_edit.add_command(label='Удалить', command=del_text)

mainmenu.add_cascade(label='Файл', menu=filemenu)
mainmenu.add_cascade(label='Шрифт', menu=file_font)
mainmenu.add_cascade(label='Правка', menu=file_edit)

text.bind('<Button-3>', popup)
text.bind('<Control-z>', undo)
text.bind('<Control-y>', redo)
text.bind('<Control-r>', replace)

menu.add_command(label='Отчисть', command=delete)
menu.add_command(label='Копировать', command=select)
menu.add_command(label='Вставить', command=paste)
menu.add_command(label='Удалить', command=del_text)
menu.add_command(label='Вырезать', command=cut)

root.mainloop()
