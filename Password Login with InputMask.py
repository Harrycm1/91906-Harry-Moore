import tkinter as tk

root = tk.Tk()
root.title("Password Entry")

password_entry = tk.Entry(root, show="*")
password_entry.pack()

root.mainloop()