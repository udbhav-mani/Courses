from tkinter import ttk
import tkinter as tk


def greet():
    print(f"Hello, {name.get() or 'World'} ")


root = tk.Tk()
root.title('Greet with python')
name = tk.StringVar()
name_label = ttk.Label(root, text="Name: ")
name_label.pack(side="left", fill="both", padx=(10, 10))
name_entry = ttk.Entry(root, textvariable=name)
name_entry.pack(side="left", fill="both", padx=(0, 10))
greet_button = ttk.Button(root, text="Greet", command=greet)
greet_button.pack(side="left", fill="both", expand=True)
name_entry.focus()

root.mainloop()
