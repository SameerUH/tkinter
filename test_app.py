"""
To-do:
--- Learn basics of frames/labels with ttk.
--- Learn basics of grids/layout.
--- Learn entry boxes.
--- Learn frames within frames.
"""

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("To-do app")

label = ttk.Label(root, text="This is a label")
label.pack()

entry = ttk.Entry(root)
entry.pack()

button = ttk.Button(root, text="Click me")
button.pack()

root.mainloop()
