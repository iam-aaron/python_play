import tkinter as tk

win = tk.Tk()
e1 = tk.Entry(win)
e1.grid(row=0, column=0, sticky='nsew')
e2 = tk.Entry(win)
e2.grid(row=1, column=0, sticky='nsew')
def calc_sum():
 the_sum = int(e1.get()) + int(e2.get())
 equals_button['text'] = str(the_sum)
equals_button = tk.Button(win, text="???", command=calc_sum)
equals_button.grid(row=2, column=0, sticky='nsew')
win.mainloop()