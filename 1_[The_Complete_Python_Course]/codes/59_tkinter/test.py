import tkinter as tk
from tkinter import ttk


def hello():
    print("Hello World")


# initializing root
root = tk.Tk()
hello_button = ttk.Button(root, text="Click me!", command=hello)
hello_button.pack(side="left", fill="x", expand=True)

quit_button = ttk.Button(root, text="Quit", command=root.destroy)
quit_button.pack(side="left", fill="x", expand=True)

root.mainloop()
