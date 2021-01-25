import tkinter as tk

root = tk.Tk()

s = tk.Canvas(master=root, width=300, height=300, bg='white')
a = s.create_oval(220, 80, 295, 5, fill='yellow',
                  activefill='orange', tag='main')

s.create_polygon(85, 275, 85, 175, 50, 175, 150,
                 125, 250, 175, 215, 175, 215, 275, fill='lightblue')

for i in range(-10, 301, 10):
    s.create_arc(i, 220, 190 + i, 400, start=180,
                 extent=-35, style=tk.ARC, outline='green', width=2)

s.tag_bind(a, '<Button-1>', lambda event: s.configure(bg='black'))
s.tag_bind(a, '<Button-3>', lambda event: s.configure(bg='white'))
s.pack()
but = tk.Button()
root.mainloop()
