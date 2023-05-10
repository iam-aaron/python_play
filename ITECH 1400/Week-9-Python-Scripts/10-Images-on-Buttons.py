import tkinter as tk
        
win = tk.Tk()

logo = tk.PhotoImage(file="python_logo.png")

B1 = tk.Button(win, image=logo, text="Woop!", compound="top")
B1.pack(padx=5, pady=5)

win.mainloop()
