"""
To-do:
--- Learn basics of frames/labels with ttk.
--- Learn basics of grids/layout.
--- Learn entry boxes.
--- Learn frames within frames.
"""

import tkinter as tk
from tkinter import ttk

root = tk.Tk()#Initializes
root.title("To-do app")
root.geometry("400x400")

style = ttk.Style()
style.configure("BW.TLabel", foreground = "black", background = "white")

l1 = ttk.Label(text = "test", style = "BW.TLabel", cursor="spraycan") #Uses the style of BW.TLabel similar to CSS
l2 = ttk.Label(text = "test", style = "BW.TLabel", font = ("Helvetica", 12, "underline"))

l1.pack()
l2.pack()

entry = ttk.Entry(root)#Text input
entry.pack()#Displays

button = ttk.Button(root, text="Click me")
button.pack()#Displays


if __name__ == "__main__":
    root.mainloop()
