import tkinter.ttk as ttk
import tkinter.messagebox as msgbox
from tkinter import *
import time

root = Tk()
root.title("my GUI")
root.geometry("640x480")

def info():
    msgbox.showinfo("Alert", "Processing complete ")

def err():
    msgbox.showerror("ERROR", "No, You can't do this ")

def warn():
    msgbox.showwarning("Warning", "ho ho ho")

def selection():
    msgbox.askokcancel("")

Button(root, command=info, text="Alert").pack()
Button(root, command=warn, text="WARN").pack()
Button(root, command=err, text="ERROR").pack()


Button(root, command=selection, text="OK CANCEL").pack()

#root.config(menu=menu)
root.mainloop()