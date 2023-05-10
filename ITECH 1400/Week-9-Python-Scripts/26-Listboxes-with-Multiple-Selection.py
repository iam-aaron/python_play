import tkinter as tk
win = tk.Tk()

items = ['One', 'Two', 'Three', 'Four']

def update_selections(event):
    selected_indices = event.widget.curselection()
    count = 0
    
    for index in selected_indices:
        print('Item: {} Index: {}'.format(items[index], index))
        count += 1

listbox = tk.Listbox(win, selectmode=tk.MULTIPLE)
listbox.bind('<<ListboxSelect>>', update_selections)

for item in items:
    listbox.insert(tk.END, item)

listbox.pack()
    
win.mainloop()
