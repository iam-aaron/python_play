import tkinter as tk
        
win = tk.Tk()

B1 = tk.Button(win, text="Hello")
B2 = tk.Button(win, text="World")

B1.place(width=100, height=100) # x and y are 0 by default
#B2.place(x=100, y=120, width=80, height=40)
B2.place(x=100, y=120, relwidth=0.3, relheight=0.3)
win.mainloop()
