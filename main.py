'''
This is the main file to run the image sorting code from.

'''

import os
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

from show_about import show_about
from file_button_menu import file_button_menu

# === Create Tkinter window ===
root = tk.Tk()
root.title('Image Sorter') # set title

# === Set default window size and location ===
# get the screen dimension
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
# find the center point
center_x = int(screen_width/2 - 900 / 2)
center_y = int(screen_height/2 - 600 / 2)
# set the position of the window to the center of the screen
root.geometry(f'900x600+{center_x}+{center_y}')

# === Create nav bar ===
navbar = tk.Frame(root, height=50)
navbar.pack(side="top", fill="x")

# === File button ===
btn_file = ttk.Menubutton(navbar, text="File")
btn_file.pack(side="left")

file_menu = tk.Menu(btn_file, tearoff=0)
file_menu.add_command(label="Open Folder...")
file_menu.add_separator()
file_menu.add_command(label="Save")
file_menu.add_command(label="Save As...")


btn_file["menu"] = file_menu

# === Edit button ===
btn_settings = ttk.Menubutton(navbar, text="Edit")
btn_settings.pack(side="left")

# === Help button ===

btn_help = tk.Button(navbar, text="Help", bd=0, padx=10)
btn_help.pack(side="left")

# === About button ===

btn_about = tk.Button(navbar, text="About", bd=0, command=lambda: show_about(root))
btn_about.pack(side="left")

# === Main frame (content area) ===
frame = tk.Frame(root, bg="grey99", relief="sunken", borderwidth=4)
frame.pack(fill="both", expand=True, padx=10, pady=10)


root.mainloop()
