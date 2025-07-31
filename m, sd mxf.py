# NCEA Credit Tracker by Harry Moore for AS91906

from tkinter import *

root = Tk()
root.title("NCEA Credit Tracker By Harry Moore")
root.geometry("500x400")
root.resizable(0, 0)

#Title font style
style = "Arial 15"

def show_frame(frame):
    frame.tkraise()

#Main Container
container = Frame(root)
container.pack(fill="both", expand=True)

#Login menu Frame
login_menu = Frame(container)
login_menu.place(relwidth=1, relheight=1)  # Stacks on container

login_title = Label(login_menu, text="NCEA Credit Tracker", font=("Arial", 21, "bold"))
login_title.pack(pady=(30, 10))

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

#Login Button
login_button = Button(login_menu, text="Enter", borderwidth=2, relief="solid", font=style, command=lambda: show_frame(main_menu))
login_button.pack(pady=20)

#Main Menu Frame
main_menu = Frame(container)
main_menu.place(relwidth=1, relheight=1)

#Main Title
main_title = Label(main_menu, text="NCEA Credit Tracker", font=("Arial", 21, "bold"))
main_title.pack(pady=(0, 10))

NA_label = Label(main_menu, text="NA Credits:")
NA_label.grid(row=1, column=0, sticky="e", padx=(20,10), pady=5)
NA_value = Label(main_menu, text="0")
NA_value.grid(row=1, column=1, sticky="w", padx=(0,10), pady=5)

A_label = Label(main_menu, text="A Credits:")
A_label.grid(row=1, column=2, sticky="e", padx=(20,10), pady=5)
A_value = Label(main_menu, text="0")
A_value.grid(row=1, column=3, sticky="w", padx=(0,10), pady=5)

M_label = Label(main_menu, text="M Credits:")
M_label.grid(row=2, column=0, sticky="e", padx=(20,10), pady=5)
M_value = Label(main_menu, text="0")
M_value.grid(row=2, column=1, sticky="w", padx=(0,10), pady=5)

E_label = Label(main_menu, text="E Credits:")
E_label.grid(row=2, column=2, sticky="e", padx=(20,10), pady=5)
E_value = Label(main_menu, text="0")
E_value.grid(row=2, column=3, sticky="w", padx=(0,10), pady=5)

#Spacer row
main_menu.grid_rowconfigure(5, minsize=40)

#Logout Button
button_frame = Frame(main_menu)
button_frame.grid(row=6, column=0, columnspan=2)
logout_button = Button(button_frame, text="Logout", borderwidth=2, relief="solid", font=style, command=lambda: show_frame(login_menu))
logout_button.pack(pady=10)

# Show login menu first
show_frame(login_menu)

root.mainloop()