'''
Given a button, this function makes it open the file browser and returns the selected directory.
'''

import tkinter as tk
from tkinter import filedialog
from tkinter.messagebox import showinfo

def open_folder(btn):
    
    folder = filedialog.askdirectory(title="Select a Folder") # opens the file browser

    return None