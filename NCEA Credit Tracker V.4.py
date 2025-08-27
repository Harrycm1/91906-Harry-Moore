#NCEA credit tracker by Harry Moore for AS91906
#PLEASE READ!!!!!!!!!!
#The username is :Harry
#And password is :Moore
from tkinter import *
import json  
import os   

root = Tk()
root.title("NCEA Credit Tracker By Harry Moore")
root.geometry("500x500")
root.resizable(0, 0)

style = "Arial 15"

def show_frame(frame):
    frame.tkraise()

container = Frame(root)
container.pack(fill="both", expand=True)

#Json file function
DATA_FILE = "credits.json"

# Now, we store totals in the file, not just latest entry
def save_data():
    data = {
        "NA_total": NA_total,
        "A_total": A_total,
        "M_total": M_total,
        "E_total": E_total
    }
    with open(DATA_FILE, "w") as f:
        json.dump(data, f)

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return {"NA_total": 0, "A_total": 0, "M_total": 0, "E_total": 0}

saved_data = load_data()

#All OF BELOW IS WINDOW 1

#Login Menu frame
login_menu = Frame(container)
login_menu.place(relwidth=1, relheight=1)

#Title
title_label = Label(login_menu, text="NCEA Credit Tracker", font=("Arial", 21, "bold"))
title_label.pack(pady=(30, 10))

#Username title and entry
username_label = Label(login_menu, text="Username:")
username_label.pack(pady=(10, 2))
username_entry = Entry(login_menu)
username_entry.pack(pady=(0, 10))

#Password title and entry
password_label = Label(login_menu, text="Password:")
password_label.pack(pady=(10, 2))
password_entry = Entry(login_menu, show="*")
password_entry.pack(pady=(0, 10))

#Check login function
def check_login():
    username = username_entry.get()
    password = password_entry.get()
    if username == "Harry" and password == "Moore":
        show_frame(main_menu)
    else:
        from tkinter import messagebox
        messagebox.showerror("Login Failed", "Incorrect username or password.")

#Login Button
Login = Button(login_menu, text="Login", borderwidth=2, relief="solid", font=style, command=check_login)
Login.pack(pady=20)

#All OF BELOW IS WINDOW 2

#Main menyu frame
main_menu = Frame(container)
main_menu.place(relwidth=1, relheight=1)

for i in range(5): 
    main_menu.grid_columnconfigure(i, weight=1)
for i in range(5): 
    main_menu.grid_rowconfigure(i, weight=1)

title_label = Label(main_menu, text="NCEA Credit Tracker", font=("Arial", 21, "bold"))
title_label.grid(row=0, column=2, pady=20, sticky="n")

#2x2 Grid
grid_frame = Frame(main_menu)
grid_frame.grid(row=1, column=1, columnspan=2, padx=5, pady=5)

#Labels and User Information
NA_label = Label(grid_frame, text="NA Credits", font=('Arial', 9, 'underline'))
NA_label.grid(row=0, column=0, padx=10, pady=10)

NA_amount = Label(grid_frame, text="0")  # Start at 0
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

#Labels and User Entries
NA_label2 = Label(grid_frame, text="Enter NA Credits")
NA_label2.grid(row=4, column=0, padx=5, pady=5)
NA_entry = Entry(grid_frame, width=3)
NA_entry.grid(row=5, column=0, padx=5, pady=5)
NA_entry.insert(0, "") 

A_label2 = Label(grid_frame, text="Enter A Credits")
A_label2.grid(row=4, column=1, padx=5, pady=5)
A_entry = Entry(grid_frame, width=3)
A_entry.grid(row=5, column=1, padx=5, pady=5)
A_entry.insert(0, "") 

M_label2 = Label(grid_frame, text="Enter M Credits")
M_label2.grid(row=6, column=0, padx=5, pady=5)
M_entry = Entry(grid_frame, width=3)
M_entry.grid(row=7, column=0, padx=5, pady=5)
M_entry.insert(0, "") 

E_label2 = Label(grid_frame, text="Enter E Credits")
E_label2.grid(row=6, column=1, padx=5, pady=5)
E_entry = Entry(grid_frame, width=3)
E_entry.grid(row=7, column=1, padx=5, pady=5)
E_entry.insert(0, "") 

#Begin at loaded values
NA_total = saved_data.get("NA_total", 0)
A_total = saved_data.get("A_total", 0)
M_total = saved_data.get("M_total", 0)
E_total = saved_data.get("E_total", 0)

# Show saved totals
NA_amount.config(text=str(NA_total))
A_amount.config(text=str(A_total))
M_amount.config(text=str(M_total))
E_amount.config(text=str(E_total))

#Calculation function
def calc():
    global NA_total, A_total, M_total, E_total
    
    try:
        na = int(NA_entry.get())
    except:
        na = 0
    try:
        a = int(A_entry.get())
    except:
        a = 0
    try:
        m = int(M_entry.get())
    except:
        m = 0
    try:
        e = int(E_entry.get())
    except:
        e = 0

    #Adding totals
    NA_total += na
    A_total += a
    M_total += m
    E_total += e

    #Update labels
    NA_amount.config(text=f"{NA_total}")
    A_amount.config(text=f"{A_total}")
    M_amount.config(text=f"{M_total}")
    E_amount.config(text=f"{E_total}")

    save_data() #Save to file!

    #Clear entries
    NA_entry.delete(0, END)
    A_entry.delete(0, END)
    M_entry.delete(0, END)
    E_entry.delete(0, END)

#Calculate button
calc_button = Button(main_menu, text="Calculate", borderwidth=2, relief="solid", font=style, command=calc)
calc_button.grid(row=8, column=2, pady=10, sticky="n")

#Logout button
back_button = Button(main_menu, text="Logout", borderwidth=2, relief="solid", font=style, command=lambda: show_frame(login_menu))
back_button.grid(row=9, column=2, pady=20, sticky="n")

show_frame(login_menu)

root.mainloop()
