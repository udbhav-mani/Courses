import tkinter as tk


root = tk.Tk()


file = open("data.txt", "+a")


def add():
    file.write(name.get() + "\n")
    name_entry.delete(0, len(name.get()))


def save():
    global file
    file.close()
    file = open("data.txt", "+a")


def save_exit():
    file.close()
    root.destroy()


name = tk.StringVar()
name_entry = tk.Entry(root, textvariable=name)
name_entry.pack(side="left", fill="both")

add_button = tk.Button(text="Add line", command=add)
add_button.pack(
    side="left",
)

save_button = tk.Button(text="Save Changes", command=save)
save_button.pack(side="left")

save_exit_button = tk.Button(text="Save Changes", command=save_exit)
save_exit_button.pack(side="left")

name_entry.focus()
root.mainloop()
