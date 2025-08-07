from tkinter import *

root = Tk()
root.title("NCEA Credit Tracker")
root.geometry("500x400")
root.resizable(0, 0)

style = "Arial 15"

#Username part
username_label = Label, text="Username:"
username_label.pack(pady=(10, 2))
username_entry = Entry
username_entry.pack(pady=(0, 10))

#Password part
password_label = Label, text="Password:"
password_label.pack(pady=(10, 2))
password_entry = Entry
password_entry.pack(pady=(0, 10))

root.mainloop()