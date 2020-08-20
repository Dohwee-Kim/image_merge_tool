from tkinter import *

root = Tk()
root.title("My GUI")
root.geometry("640x480")


chkvar = IntVar() #save the inttype value to the variable chkvar 
chkbox = Checkbutton(root, text="Do not show again today", variable=chkvar)
#chkbox.select() #auto selected 
#chkbox.deselect() #de select 
chkbox.pack()

chkvar2 = IntVar() #save the inttype value to the variable chkvar2
chkbox2 = Checkbutton(root, text="Do not show again this week", variable=chkvar2)
chkbox2.pack()


def btncmd():
    #print(chkvar.get())
    #print(chkvar2.get())


btn = Button(root,text= "Click", command=btncmd)
btn.pack()

root.mainloop()