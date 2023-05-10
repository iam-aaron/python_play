import tkinter as tk
from tkinter import Label
import os
os.environ['TK_SILENCE_DEPRECATION'] = '1'

# Create a new window
window = tk.Tk()

# Set the window title
window.title("My Tkinter Window")

# Set the window size
window.geometry("400x300")

# Create a label widget
label = tk.Label(window, text="Hello, Tkinter!")

# Pack the label widget into the window
label.pack()

# # Create a button widget
# button = tk.Button(window, text="Click me!", command=window.destroy)

# # Pack the button widget into the window
# button.pack()

# Run the event loop
window.mainloop()