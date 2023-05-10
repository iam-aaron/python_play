import tkinter as tk

counter = 0

def incrementCounter(event):
   global counter
   counter += 1
   event.widget.configure( text = str(counter) )


def main():
    win = tk.Tk()
    b = tk.Button(win, text='Click to start counting!')
    b.grid(row=0,column=1)
    b.pack()
    b.bind('<Button-1>', incrementCounter)
    win.mainloop()

# main function
if __name__ == "__main__": # if this file is run directly, run main()
    main()