import tkinter as tk
        
win = tk.Tk()

B1 = tk.Button(win, text="Red", bg="red", fg="white")
B1.pack(side=tk.LEFT)
B2 = tk.Button(win, text="Green", bg="green", fg="white")
B2.pack(side=tk.LEFT)
B3 = tk.Button(win, text="Blue", bg="blue", fg="white")
B3.pack(side=tk.LEFT)
            
win.mainloop()
