import tkinter as tk
        
win = tk.Tk()

B1 = tk.Button(win, text="1")
B2 = tk.Button(win, text="2")
B3 = tk.Button(win, text="3")
B4 = tk.Button(win, text="4")
B5 = tk.Button(win, text="5")
B6 = tk.Button(win, text="6")

B1.grid(row=0, column=0, columnspan=2)
B2.grid(row=1, column=0)
B3.grid(row=1, column=1)
B4.grid(row=1, column=2, rowspan=2)
B5.grid(row=2, column=0)
B6.grid(row=2, column=1)

win.columnconfigure(0, weight=1)
win.columnconfigure(1, weight=1)
win.columnconfigure(2, weight=1)
            
win.mainloop()
