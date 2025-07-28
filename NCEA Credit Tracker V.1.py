from tkinter import *
root = Tk()
root.title("NCEA Credit Tracker")
root.geometry("500x400")
root.resizable(0, 0)

style = "Arial 15"

def show_frame(frame):
    frame.tkraise()

#Main container frame
container = Frame(root)
container.pack(fill="both", expand=True)

#Frame 1: Login Menu
login_menu = Frame(container)
login_menu.grid(relwidth=1, relheight=1)

title_label = Label(login_menu, text="NCEA Credit Tracker", font=("Arial", 21, "bold"))
title_label.grid(row=0, column=0)

#Username part
username_label = Label(root, text="username:")
username_label.grid(row=1, column=0)

username_entry = Entry(root)
username_entry.grid(row=1, column=1)


#Button rows
button_frame = Frame(login_menu)
button_frame.pack()

Login = Button(button_frame, text="Enter", borderwidth=2.5, relief="solid", font=style, command=lambda: show_frame(Main_menu))
Login.pack(padx=10)

#Frame 2: Credit tracker menu
Main_menu = Frame(container)
Main_menu.place(relwidth=1, relheight=1)

Button(Main_menu, text="Back", borderwidth=2, relief="solid", command=lambda: show_frame(login_menu)).pack()

#Show main menu initially
show_frame(login_menu)

root.mainloop()
