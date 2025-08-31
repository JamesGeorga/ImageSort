'''
This function populates a dropdown menu provided the list of elements to be contained in it as labels.

'''

import tkinter as tk

def populate_menu(button, labels):

    menu = tk.Menu(button, tearoff=0)

    for word in labels:
        if word == "separator":
            menu.add_separator()
        else:
            menu.add_command(label=word)
    
    button["menu"] = menu

    return menu