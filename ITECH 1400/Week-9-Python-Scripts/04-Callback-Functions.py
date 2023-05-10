import tkinter

win = tkinter.Tk()

def quit():
    win.destroy()

from tkinter import Button
widget = Button(win, text='Click me!', command=quit)
widget.pack()

win.mainloop()
