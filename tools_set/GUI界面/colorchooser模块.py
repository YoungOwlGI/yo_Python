import tkinter as tk
from tkinter import colorchooser


def choose_color():
    color = colorchooser.askcolor(title="选择颜色")
    print("Selected color:", color)


root = tk.Tk()
root.geometry("300x100")

button = tk.Button(root, text="选择颜色", command=choose_color)
button.pack(pady=20)

root.mainloop()
