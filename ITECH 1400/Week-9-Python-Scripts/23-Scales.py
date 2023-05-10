import tkinter as tk        
win = tk.Tk()

vertVal = tk.IntVar()
horizVal = tk.IntVar()

def onMove(value):
    print('Current value: {}'.format(value))

vertScale  = tk.Scale(win, from_=0, to=30, variable=vertVal,
                      command=onMove, tickinterval=10).pack()
horizScale = tk.Scale(win, from_=100, to=200, variable=horizVal,
                      command=onMove, orient=tk.HORIZONTAL).pack()

win.mainloop()

