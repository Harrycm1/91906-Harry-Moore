from tkinter import *

root = Tk()
root.title("NCEA Credit Tracker")
root.geometry("500x400")
root.resizable(0, 0)

style = "Arial 15"

def show_frame(frame):
    frame.tkraise()

# Main container frame
container = Frame(root)
container.pack(fill="both", expand=True)

#Login menu frame
login_menu = Frame(container)
login_menu.place(relwidth=1, relheight=1)

title_label = Label(login_menu, text="NCEA Credit Tracker", font=("Arial", 21, "bold"))
title_label.pack(pady=(30, 10))

#Username part
username_label = Label(login_menu, text="Username:")
username_label.pack(pady=(10, 2))
username_entry = Entry(login_menu)
username_entry.pack(pady=(0, 10))

#Enter Button
Login = Button(login_menu, text="Enter", borderwidth=2.5, relief="solid", font=style, command=lambda: show_frame(main_menu))
Login.pack(pady=20)

#Main menu frame
main_menu = Frame(container)
main_menu.place(relwidth=1, relheight=1)

back_button = Button(main_menu, text="Back", borderwidth=2, relief="solid", font=style, command=lambda: show_frame(login_menu))
back_button.pack(pady=20)

#show login menu first
show_frame(login_menu)

root.mainloop()
