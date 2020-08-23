import tkinter.ttk as ttk
from tkinter import *
import time

root = Tk()
root.title("my GUI")
root.geometry("640x480")


def create_new_file():
    print("Creating a new file")

def open_new_file():
    print("Open a new file")

menu = Menu(root)
menu_file = Menu(menu, tearoff=0)
menu_file.add_command(label="New File", command= create_new_file)
menu_file.add_command(label="New Window")
menu_file.add_separator()
menu_file.add_command(label="Open File...", command = open_new_file)

menu_file.add_command(label="Save All", state="disable") #
menu_file.add_separator()
menu_file.add_command(label="Exit", command= root.quit)
menu.add_cascade(label="File", menu=menu_file)
#second casecade menu 
menu.add_cascade(label="Edit") 

#Adding language menu 
menu_lang = Menu(menu, tearoff=0)
menu_lang.add_radiobutton(label="Python")
menu_lang.add_radiobutton(label="Java")
menu_lang.add_radiobutton(label="C++")
menu.add_cascade(label="Programming Language", menu=menu_lang) 

#checkbox 
menu_view = Menu(menu, tearoff=0)
menu_view.add_checkbutton(label="Show Minimap")
menu.add_cascade(label="View", menu=menu_view)

root.config(menu=menu)


root.mainloop()