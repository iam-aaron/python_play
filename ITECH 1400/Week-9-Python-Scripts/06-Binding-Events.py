import tkinter
from tkinter import Button

win = tkinter.Tk()

def clicked(event):
    event.widget['text'] = 'Left clicked!'

def quit(event):
    event.widget.configure(text='Right clicked!')
    # win.destroy()

b = Button(win, text='Click me!')
b.pack()
b.bind('<Button-1>', clicked) # LMB click handler
b.bind('<Button-2>', quit)    # RMB click handler


win.mainloop()
