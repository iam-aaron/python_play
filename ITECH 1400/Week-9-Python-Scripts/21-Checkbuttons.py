import tkinter as tk
        
win = tk.Tk()

wantBreakfast = tk.IntVar();
wantLunch     = tk.IntVar();
wantDinner    = tk.IntVar();

def handle_cb():
    print("Breakfast: {}".format(wantBreakfast.get()))
    print("Lunch: {}".format(wantLunch.get()))
    print("Dinner: {}".format(wantDinner.get()))    

CB1 = tk.Checkbutton(win, text="Breakfast",
                     variable=wantBreakfast, command=handle_cb).pack()
CB2 = tk.Checkbutton(win, text="Lunch",
                     variable=wantLunch, command=handle_cb).pack()
CB3 = tk.Checkbutton(win, text="Dinner",
                     variable=wantDinner, command=handle_cb).pack()
               
win.mainloop()
