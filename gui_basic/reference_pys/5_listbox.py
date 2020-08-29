from tkinter import *

root = Tk()
root.title("My GUI")
root.geometry("640x480")

#  selectmode extended = multple choice, single = only one 
# height = 0 shows everything, int = how many lines 
listbox = Listbox(root, selectmode="extended", height=0)
listbox.insert(0,"apple")
listbox.insert(1,"strawberry")
listbox.insert(2,"banana")
listbox.insert(END,"watermelon")
listbox.insert(END,"grape")
listbox.pack()

def btncmd():
    #Deletion 
    #listbox.delete(END) # delete the last element
    #listbox.delete(0) #delete the first one 

    #check the size 
    #print(listbox.size())

    # check the values 
    #print(listbox.get(0,2))

    # check the selected value 
    #print("selected one: " , listbox.curselection())  # returns indices 



btn = Button(root,text= "Click", command=btncmd)
btn.pack()

root.mainloop()