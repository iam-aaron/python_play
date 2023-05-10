import tkinter as tk
from tkinter import messagebox
win = tk.Tk()
uname_label = tk.Label(win, text="Username")
uname_field = tk.Entry(win)
passw_label = tk.Label(win, text="Password")
passw_field = tk.Entry(win, show="*")
login_button = tk.Button(win, text="Login")
uname = ""
passw = ""
VALID_USERNAME = "username"
VALID_PASSWORD = "password"


def login(event):
    uname = uname_field.get()
    passw = passw_field.get()
    
    if ( uname == VALID_USERNAME and passw == VALID_PASSWORD):
        tk.messagebox.showinfo('Success', 'Log in successful!')
    else:
        tk.messagebox.showerror('Login failed', 'Bad username or password.')

def main():
    uname_label.grid(row=0, column=0, sticky=tk.E)
    uname_field.grid(row=0, column=1, sticky=tk.W)
    passw_label.grid(row=1, column=0, sticky=tk.E)
    passw_field.grid(row=1, column=1, sticky=tk.W)
    login_button.grid(row=2, column=0, columnspan=2, sticky="nsew")

    login_button.bind('<Button-1>', login)

    win.mainloop()


# main function
if __name__ == "__main__": # if this file is run directly, run main()
    main()