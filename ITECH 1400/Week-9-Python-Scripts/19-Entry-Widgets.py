import tkinter as tk
        
win = tk.Tk()
entry = tk.Entry(win)

def print_entry():
    print( entry.get() )

entry = tk.Entry(win)
button = tk.Button(win, text="Print", command=print_entry)

entry.pack()
button.pack()

win.mainloop()
