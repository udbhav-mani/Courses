from tkinter import ttk
import tkinter as tk

root = tk.Tk()
root.title("Learn Packing")
tk.Label(root, bg="green", text="Label 1").pack(side="left", fill="y", expand=True)

tk.Label(root, bg="red", text="Label 1").pack(side="top", fill="x")
# tk.Label(root, bg="red", text="Label 2").pack(fill="both", side="left")
# tk.Label(root, bg="pink", text="Label 3").pack(fill="both", side="left", expand=True)
# tk.Label(root, bg="blue", text="Label 4").pack(fill="both", side="top", expand=True)

root.mainloop()
