import tkinter as tk

win = tk.Tk()

canvas = tk.Canvas(win, width=640, height=480, bg="pink")

# Note: Params for 2D shapes are (left, top), (right, bottom)
arc_coords = [400, 50, 600, 250]
arc = canvas.create_arc(arc_coords, start=45, extent=270, fill="yellow")

line      = canvas.create_line(100, 100, 300, 300, fill="red", dash=(8,2))
rectangle = canvas.create_rectangle(20, 25, 310, 75, fill="blue")
oval      = canvas.create_oval(300, 350, 600, 450, fill="black")
text      = canvas.create_text(165, 50, font="arial 16 bold", text="If I jump I'll be okay, I think!")

picture = tk.PhotoImage(file='potato.png')
bitmap    = canvas.create_image(300, 300, image=picture)

canvas.pack()

win.mainloop()
