import tkinter as tk


class Rainbow:
    def __init__(self, color):
        self.but = tk.Button(master=frame, width=3, height=1, bg=hex_color.get(color), command=self.color_m)
        self.color = color
        self.but.pack(side='left', padx=2, pady=5)

    def color_m(self):
        lab['text'] = self.color
        ent.delete(0, tk.END)
        ent.insert(0, hex_color.get(self.color))


root = tk.Tk()
root.resizable(0, 0)
lab = tk.Label(width=20, justify='center')
ent = tk.Entry(width=20, justify='center')
frame = tk.LabelFrame(width=40, height=3, text='Colors:')
lab.pack(pady=3)
ent.pack(pady=6)
frame.pack()
hex_color = {'red': '#ff0000', 'orange': '#ffa500', 'yellow': '#ffff00', 'green': '#008000',
             'blue': '#0000ff', 'indigo': '#4b0082', 'violet': '#ee82ee'}

for i in hex_color.keys():
    Rainbow(i)

tk.mainloop()
