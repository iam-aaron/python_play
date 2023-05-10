import tkinter as tk
        
win = tk.Tk()
label = tk.Label(win, text="Best current gen console?").pack()
consoles = ['Xbox One X', 'PS4 Pro', 'Nintendo Switch']
answer = tk.StringVar()

def handle_rb():
    index = int( answer.get() )
    print("User preference: {} (index {})".format(consoles[index], index))

count = 0
for console in consoles:
    rb = tk.Radiobutton(win, text=console, value=count,
                        variable=answer, command=handle_rb)
    count += 1
    rb.pack()

# Select first radiobutton as default option
answer.set(0)

win.mainloop()
