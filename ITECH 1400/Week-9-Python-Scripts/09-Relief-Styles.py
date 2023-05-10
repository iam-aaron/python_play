import tkinter as tk
from tkinter import *

win = tk.Tk()

B1 = Button(win, text = "FLAT",   relief = tk.FLAT   )
B2 = Button(win, text = "RAISED", relief = tk.RAISED )
B3 = Button(win, text = "SUNKEN", relief = tk.SUNKEN )
B4 = Button(win, text = "GROOVE", relief = tk.GROOVE )
B5 = Button(win, text = "RIDGE",  relief = tk.RIDGE  )

B1.pack()
B2.pack()
B3.pack()
B4.pack()
B5.pack()
            
win.mainloop()
