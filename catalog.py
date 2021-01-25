import tkinter as tk


def add_box():
    things_id = list(shop_list.curselection())
    things_id.reverse()
    for el in things_id:
        user_list.insert(0, shop_list.get(el))
        shop_list.delete(el)


def drop_box():
    things_id = list(user_list.curselection())
    things_id.reverse()
    for el in things_id:
        shop_list.insert(0, user_list.get(el))
        user_list.delete(el)


f1 = tk.Frame(width=40, height=20)
f1.pack(side=tk.LEFT, fill=tk.BOTH, pady=5, padx=5)
f2 = tk.Frame(width=40, height=20)
f2.pack(side=tk.LEFT, fill=tk.BOTH, padx=5, pady=50)
f3 = tk.Frame(width=40, height=20, pady=5, padx=5)
f3.pack(side=tk.LEFT, fill=tk.BOTH)
tk.Label(master=f1, text='Каталог').pack()
tk.Label(master=f3, text='Корзина').pack()
shop_list = tk.Listbox(master=f1, selectmode=tk.EXTENDED)
shop_list.pack(side=tk.LEFT, fill=tk.BOTH)
user_list = tk.Listbox(master=f3, selectmode=tk.EXTENDED)
user_list.pack(side=tk.LEFT, fill=tk.BOTH)

scroll1 = tk.Scrollbar(master=f1, command=shop_list.yview)
scroll1.pack(side=tk.RIGHT, fill=tk.Y)
shop_list.config(yscrollcommand=scroll1.set)

scroll2 = tk.Scrollbar(master=f3, command=user_list.yview)
scroll2.pack(side=tk.RIGHT, fill=tk.Y)
user_list.config(yscrollcommand=scroll2.set)

tk.Button(master=f2, width=7, text='>>', command=add_box).pack()
tk.Button(master=f2, width=7, text='<<', command=drop_box).pack()

for i in ('apple', 'milk', 'beer', 'tomato', 'cucumber', 'orange', 'eggs', 'bread', 'meat', 'sausage', 'cola'):
    shop_list.insert(0, i)

tk.mainloop()
