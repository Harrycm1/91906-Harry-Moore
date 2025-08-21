import tkinter as tk

def create_gui():
    root = tk.Tk()
    root.title("Entry to Label Example (Button)")

    # Create the Entry widget
    entry = tk.Entry(root)
    entry.pack(pady=10)

    # Create the Label widget (initially empty)
    label = tk.Label(root, text="")
    label.pack(pady=10)

    def update_label():
        # Get the text from the Entry widget
        entered_text = entry.get()
        # Update the Label's text
        label.config(text=f"You entered: {entered_text}")
        # Optionally, clear the Entry after getting the text
        entry.delete(0, tk.END) 

    # Create a button to trigger the update
    button = tk.Button(root, text="Display Entry", command=update_label)
    button.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    create_gui()