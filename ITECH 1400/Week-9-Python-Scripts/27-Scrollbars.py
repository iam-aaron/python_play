import tkinter as tk
win = tk.Tk()

scrollbar = tk.Scrollbar(win)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

listbox = tk.Listbox(win, yscrollcommand=scrollbar.set)

for i in range(1000):
    listbox.insert(tk.END, str(i))

listbox.pack(side=tk.LEFT, fill=tk.BOTH)
scrollbar.config(command=listbox.yview)

win.mainloop()
