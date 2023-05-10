import tkinter as tk
        
win = tk.Tk()

B1 = tk.Button(win, text = "Error",     bitmap = "error"    , compound="left")
B2 = tk.Button(win, text = "Hourglass", bitmap = "hourglass", compound="left")
B3 = tk.Button(win, text = "Info",      bitmap = "info"     , compound="left")
B4 = tk.Button(win, text = "Question",  bitmap = "question" , compound="left")
B5 = tk.Button(win, text = "Warning",   bitmap = "warning"  , compound="left")

B1.pack()
B2.pack()
B3.pack()
B4.pack()
B5.pack()
            
win.mainloop()
