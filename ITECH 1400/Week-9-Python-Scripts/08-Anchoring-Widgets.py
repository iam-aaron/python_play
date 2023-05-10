import tkinter as tk

win = tk.Tk()
win.geometry('200x150')

right = tk.Label(win, text="Right", bg="light blue")
right.pack(side=tk.RIGHT)

left = tk.Label(win, text = "Left", bg="green")
left.pack(side=tk.LEFT)

bottom = tk.Label(win, text="Bottom", bg="red")
bottom.pack(side=tk.BOTTOM, anchor=tk.W)

top = tk.Label(win, text="Top", bg="pink")
top.pack(side=tk.TOP, anchor=tk.E)

win.mainloop()
