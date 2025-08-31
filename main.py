'''
This is the main file to run the image sorting code from.

'''

import os
import tkinter as tk # use tkinter to build GUI
from tkinter import ttk, filedialog
from PIL import Image, ImageTK # Use pillow to display images

# external functions
from show_about import show_about
from show_help import show_help
from create_menu import create_menu
from load_images import load_images

def open_folder():
    
    folder = filedialog.askdirectory(title="Select a Folder") # opens the file browser

    root.selected_folder.set(folder)


# === Create Tkinter window ===
root = tk.Tk()
root.title('Image Sorter') # set title
root.selected_folder = tk.StringVar(value="No folder selected.") # store current folder location (None by defualt)

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

# === File Button Menu ===
btn_file = ttk.Menubutton(navbar, text="File")
btn_file.pack(side="left")

file_menu = create_menu(btn_file, ["Open Folder...", "separator", "Save", "Save As...", "separator", "Exit"]) # Use function to populate menu
file_menu.entryconfig(file_menu.index("Open Folder...", ), command=lambda: open_folder()) # Add 'Open Folder' functionality
# file_menu.entryconfig(file_menu.index("Save", ))

# === Edit button menu ===
btn_settings = ttk.Menubutton(navbar, text="Edit")
btn_settings.pack(side="left")

settings_menu = create_menu(btn_settings, ["Undo", "Redo", "separator", "Copy", "Paste"])

# === Help button ===
btn_help = tk.Button(navbar, text="Help", bd=0, padx=10, command=lambda: show_help(root))
btn_help.pack(side="left")

# === About button ===
btn_about = tk.Button(navbar, text="About", bd=0, command=lambda: show_about(root))
btn_about.pack(side="left")

# === Main frame (content area) ===
frame = tk.Frame(root, bg="grey99", relief="sunken", borderwidth=4)
frame.pack(fill="both", expand=True, padx=10)

# display images in current directory


# === Current Directory ===
direc = tk.Frame(root, height=50)
direc.pack(side="bottom", fill="x")
label = tk.Label(direc, textvariable=root.selected_folder) # test folder can be found.
label.pack(side="left")

root.mainloop()