import tkinter as tk
        
win = tk.Tk()


L1 = tk.Label(win,text="First")
E1 = tk.Entry(win)
L2 = tk.Label(win,text="Second")
E2 = tk.Entry(win)

L1.grid(row=0, column=0, sticky=tk.W)
E1.grid(row=0, column=1)
L2.grid(row=1, column=0, sticky=tk.W)
E2.grid(row=1, column=1)
            
win.mainloop()
