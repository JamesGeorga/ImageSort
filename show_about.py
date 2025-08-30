'''
This is the function code for the about button.
'''

import tkinter as tk
import webbrowser

def show_about(root):
    # Create floating window
    about_win = tk.Toplevel(root)
    about_win.title("About Image Sorter")
    about_win.geometry("300x200")
    about_win.resizable(False, False)  # stop resizing

    # Center it relative to the root window
    root_x = root.winfo_x()
    root_y = root.winfo_y()
    root_w = root.winfo_width()
    root_h = root.winfo_height()
    win_w, win_h = 300, 200
    pos_x = root_x + (root_w // 2) - (win_w // 2)
    pos_y = root_y + (root_h // 2) - (win_h // 2)
    about_win.geometry(f"{win_w}x{win_h}+{pos_x}+{pos_y}")

    # Add content
    label = tk.Label(about_win, text="Image Sorter v0.0.1\nCreated by James Georgaras")
    label.pack(pady=40)
    link = tk.Label(about_win, text="https://github.com/JamesGeorga/ImageSort", fg="blue", cursor="hand2")
    link.pack()
    link.bind("<Button-1>", lambda e: webbrowser.open_new("https://github.com/JamesGeorga/ImageSort"))


    close_btn = tk.Button(about_win, text="Close", command=about_win.destroy)
    close_btn.pack(pady=10)

    # Keep this window above root
    about_win.transient(root)  
    about_win.grab_set()       # modal behavior (blocks root until closed)
    root.wait_window(about_win)

