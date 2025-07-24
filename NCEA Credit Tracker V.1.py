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

#Frame 1: Main Menu
frame_main = Frame(container)
frame_main.place(relwidth=1, relheight=1)

title_label = Label(frame_main, text="NCEA Credit Tracker", font=("Arial", 21, "bold"))

title_label.pack(pady=10)

#Button row 
button_frame = Frame(frame_main)
button_frame.pack()

btn_cent = Button(button_frame, text="to Centigrade", bg="yellow", font=style, command=lambda: show_frame(frame_cent))
btn_cent.pack(side=LEFT, padx=10)

btn_fahr = Button(button_frame, text="to Fahrenheit", bg="red", font=style, command=lambda: show_frame(frame_fahr))
btn_fahr.pack(side=LEFT, padx=10)

#Frame 2: To Centigrade
frame_cent = Frame(container)
frame_cent.place(relwidth=1, relheight=1)

Button(frame_cent, text="Back", command=lambda: show_frame(frame_main)).pack()

#Frame 3: To Fahrenheit
frame_fahr = Frame(container)
frame_fahr.place(relwidth=1, relheight=1)
Button(frame_fahr, text="Back", command=lambda: show_frame(frame_main)).pack()

#Show main menu initially
show_frame(frame_main)

root.mainloop()