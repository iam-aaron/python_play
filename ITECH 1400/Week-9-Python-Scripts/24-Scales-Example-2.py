import tkinter as tk

win = tk.Tk()
win.geometry('400x200')

label = tk.Label(win, text='Hello, World!', font='helvetica 12 bold')
label.pack(fill=tk.Y, expand=1)

fontSize = tk.IntVar()

def resizeFont(value):
    fontString = 'helvetica {} bold'.format(value)
    label.config(font=fontString)

fontScale = tk.Scale(win, from_=12, to=48, variable=fontSize,
                      command=resizeFont, orient=tk.HORIZONTAL).pack()

win.mainloop()
