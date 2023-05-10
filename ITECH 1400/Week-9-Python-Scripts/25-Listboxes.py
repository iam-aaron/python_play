import tkinter as tk

win = tk.Tk()

# Note: You cannot append .pack to this - pack after adding!
listbox = tk.Listbox(win)

items = ['One', 'Two', 'Three', 'Four']

for item in items:
    listbox.insert(tk.END, item)

listbox.select_set(2) # Select item at index two
listbox.pack()
    
win.mainloop()
