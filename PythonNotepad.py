# Ejike Etolue A. 
# NCAIR Python Beginner Class
# Final Project: Create a Python Notepad

import tkinter as tk
from tkinter import filedialog

# Function definitions
def new_file():
    """Clears the text box."""
    text_box.delete("1.0", "end")


def open_file():
    """Opens a file and loads its contents into the text box."""
    file_path = filedialog.askopenfilename(title="Open File")
    if file_path:
        with open(file_path, 'r') as file:
            text_box.insert("1.0", file.read())


def save_file():
    """Saves the contents of the text box to the current file."""
    file_path = filedialog.asksaveasfilename(title="Save File")
    if file_path:
        with open(file_path, 'w') as file:
            file.write(text_box.get("1.0", "end"))


def save_as_file():
    """Saves the contents of the text box to a new file."""
    file_path = filedialog.asksaveasfilename(title="Save As")
    if file_path:
        with open(file_path, 'w') as file:
            file.write(text_box.get("1.0", "end"))


# Create the main window
root = tk.Tk()
root.title("Python Notepad")
root.geometry("500x300")

# Create the text box
text_box = tk.Text(root, width=50, height=20)
text_box.pack(expand=True, fill='both')

# Create a menu bar
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

# Create a "File" menu
file_menu = tk.Menu(menu_bar, tearoff=True)

# Add menu items to the "File" menu
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_command(label="Save As", command=save_as_file)
file_menu.add_command(label="Exit", command=root.quit)

# Add the "File" menu to the menu bar
menu_bar.add_cascade(label="File", menu=file_menu)

# Start the main event loop
root.mainloop()