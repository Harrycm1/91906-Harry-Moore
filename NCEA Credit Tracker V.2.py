#NCEA credit tracker by Harry Moore for AS91906

from tkinter import *

root = Tk()
root.title("NCEA Credit Tracker By Harry Moore")
root.geometry("500x400")
root.resizable(0, 0)

#Title font
style = "Arial 15"

def show_frame(frame):
    frame.tkraise()

#Main container frame
container = Frame(root)
container.pack(fill="both", expand=True)


#ALL OF BELOW IS WINDOW 1

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

#Password part
password_label = Label(login_menu, text="Password:")
password_label.pack(pady=(10, 2))
password_entry = Entry(login_menu, show="*")
password_entry.pack(pady=(0, 10))

#Enter Button
Login = Button(login_menu, text="Enter", borderwidth=2, relief="solid", font=style, command=lambda: show_frame(main_menu))
Login.pack(pady=20)

#Main menu frame
main_menu = Frame(container)
main_menu.place(relwidth=1, relheight=1)


#ALL OF BELOW IS WINDOW 2

#Main Title
title_label = Label(main_menu, text="NCEA Credit Tracker", font=("Arial", 21, "bold"))
title_label.grid(row=0, column=0, pady=20)

NA_label = Label(main_menu, text="NA Credits")
NA_label.grid(row=1, column=1, padx=20)

A_label = Label(main_menu, text="A Credits")
A_label.grid(row=1, column=2)

M_label = Label(main_menu, text="M Credits")
M_label.grid(row=2, column=1, padx=20)

E_label = Label(main_menu, text="E Credits")
E_label.grid(row=2, column=2)



back_button = Button(main_menu, text="Logout", borderwidth=2, relief="solid", font=style, command=lambda: show_frame(login_menu))
back_button.grid()

#show login menu first
show_frame(login_menu)

root.mainloop()
