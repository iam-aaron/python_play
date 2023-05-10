import tkinter

win = tkinter.Tk()

from tkinter import Button
widget = Button(win, text='Click me!', command=win.destroy)
widget.pack()

win.mainloop()
