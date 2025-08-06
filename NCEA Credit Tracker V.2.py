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

#Main menu frame
main_menu = Frame(container)
main_menu.place(relwidth=1, relheight=1)

#Row and column centre thingy
for i in range(5): 
    main_menu.grid_columnconfigure(i, weight=1)
for i in range(5): 
    main_menu.grid_rowconfigure(i, weight=1)

#Main Title 
title_label = Label(main_menu, text="NCEA Credit Tracker", font=("Arial", 21, "bold"))
title_label.grid(row=0, column=2, pady=20, sticky="n")

#2x2 Frame for below
grid_frame = Frame(main_menu)
grid_frame.grid(row=1, column=1, columnspan=2, padx=20, pady=20)

#2x2 gridding
NA_label = Label(grid_frame, text="NA Credits")
NA_label.grid(row=0, column=0, padx=10, pady=10)

A_label = Label(grid_frame, text="A Credits")
A_label.grid(row=0, column=1, padx=10, pady=10)

M_label = Label(grid_frame, text="M Credits")
M_label.grid(row=1, column=0, padx=10, pady=10)

E_label = Label(grid_frame, text="E Credits")
E_label.grid(row=1, column=1, padx=10, pady=10)

#Logout button
back_button = Button(main_menu, text="Logout", borderwidth=2, relief="solid", font=style, command=lambda: show_frame(login_menu))
back_button.grid(row=3, column=2, pady=20, sticky="n")

#show login menu first
show_frame(login_menu)

root.mainloop()
