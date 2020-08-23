import tkinter.ttk as ttk
from tkinter import *

root = Tk()
root.title("my GUI")
root.geometry("640x480")

values= ["day " + str(i) for i in range(1,32)]  #1 ~ 31 , type casting to str 
combobox = ttk.Combobox(root, height =5, values =values)
combobox.pack()
combobox.set("Transaction date") # initial list 


combobox_readonly = ttk.Combobox(root, height =10, values =values, state = "readonly")
#combobox_readonly.set("Transaction date : Read only") # initial list 
combobox_readonly.current(0) #choose 0th
combobox_readonly.pack()




def btncmd():
    print(combobox.get()) # printout chosen date 
    print(combobox_readonly.get()) # printout chosen date 

btn = Button(root, text="Choose", command = btncmd)
btn.pack()
root.mainloop()