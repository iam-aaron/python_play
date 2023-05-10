import tkinter
from tkinter import Button

win = tkinter.Tk()

class QuitButton:
    def __init__(self):
        widget = Button(win, text='Quit!', command=self.quit)
        widget.pack()        

    def quit(self):
        win.destroy()

QuitButton()
win.mainloop()
