import tkinter as tk
        
win = tk.Tk()

B1 = tk.Button(win, text="1")

def increaseNumber(event):
    number = int( B1['text'] )
    number += 1
    B1['text'] = str(number)


B1.bind('<Button-1>', increaseNumber)
B1.pack()
            
win.mainloop()
