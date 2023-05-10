import tkinter as tk
        
win = tk.Tk()

leftFrame = tk.Frame(win, width=100, height=100, bg="green")
rightFrame = tk.Frame(win, padx=20, pady=20, bg="blue")

leftFrame.pack(side=tk.LEFT)
rightFrame.pack(side=tk.RIGHT)

B1 = tk.Button(rightFrame, text="1").pack()
B2 = tk.Button(rightFrame, text="2").pack()
B3 = tk.Button(rightFrame, text="3").pack()
               
win.mainloop()
