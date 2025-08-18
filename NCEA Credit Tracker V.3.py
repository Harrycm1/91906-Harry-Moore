#NCEA credit tracker by Harry Moore for AS91906
#PLEASE READ!!!!!!!!!!
#The username is :Harry
#And password is :Moore

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

#Login function which checks users inputs above to make sure they enter the correct username and password
def check_login():
    username = username_entry.get()
    password = password_entry.get()
    if username == "Harry" and password == "Moore":
        show_frame(main_menu)
    else:
        from tkinter import messagebox
        messagebox.showerror("Login Failed", "Incorrect username or password.")

#Logiin button
Login = Button(login_menu, text="Login", borderwidth=2, relief="solid", font=style, command=check_login)
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

#2x2 for frame
grid_frame = Frame(main_menu)
grid_frame.grid(row=1, column=1, columnspan=2, padx=20, pady=20)

#2x2 gridding
NA_label = Label(grid_frame, text="NA Credits", font=('Arial', 9, 'underline'))
NA_label.grid(row=0, column=0, padx=10, pady=10)

NA_amount = Label(grid_frame, text="0")
NA_amount.grid(row=1, column=0, padx=5, pady=5)

A_label = Label(grid_frame, text="A Credits", font=('Arial', 9, 'underline'))
A_label.grid(row=0, column=1, padx=10, pady=10)

A_amount = Label(grid_frame, text="0")
A_amount.grid(row=1, column=1, padx=5, pady=5)

M_label = Label(grid_frame, text="M Credits", font=('Arial', 9, 'underline'))
M_label.grid(row=2, column=0, padx=10, pady=10)

M_amount = Label(grid_frame, text="0")
M_amount.grid(row=3, column=0, padx=5, pady=5)

E_label = Label(grid_frame, text="E Credits", font=('Arial', 9, 'underline'))
E_label.grid(row=2, column=1, padx=10, pady=10)

E_amount = Label(grid_frame, text="0")
E_amount.grid(row=3, column=1, padx=5, pady=5)

#User entry for Labels above
grid_frame = Frame(main_menu)
grid_frame.grid(row=4, column=1, columnspan=2, padx=20, pady=20)

NA_label2 = Label(grid_frame, text="Enter NA Credits")
NA_label2.grid(row=4, column=0, padx=5, pady=5)

NA_entry = Entry(grid_frame)
NA_entry.grid(row=5, column=0, padx=5, pady=5)

A_label2 = Label(grid_frame, text="Enter A Credits")
A_label2.grid(row=4, column=1, padx=5, pady=5)

A_entry = Entry(grid_frame)
A_entry.grid(row=5, column=1, padx=5, pady=5)

M_label2 = Label(grid_frame, text="Enter M Credits")
M_label2.grid(row=6, column=0, padx=5, pady=5)

M_entry = Entry(grid_frame)
M_entry.grid(row=7, column=0, padx=5, pady=5)

E_label2 = Label(grid_frame, text="Enter E Credits")
E_label2.grid(row=6, column=1, padx=5, pady=5)

E_entry = Entry(grid_frame)
E_entry.grid(row=7, column=1, padx=5, pady=5)


#Logout button
back_button = Button(main_menu, text="Logout", borderwidth=2, relief="solid", font=style, command=lambda: show_frame(login_menu))
back_button.grid(row=8, column=2, pady=20, sticky="n")

#show login menu first
show_frame(login_menu)

root.mainloop()
