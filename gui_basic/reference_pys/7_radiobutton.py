from tkinter import *

root = Tk()
root.title("My GUI")
root.geometry("640x480")

label1 = Label(root, text="select your main menu")
label1.pack()


burger_var = IntVar()
btn_burger1 = Radiobutton(root, text="Hamburger", value=1, variable=burger_var)
btn_burger2 = Radiobutton(root, text="Vegiburger", value=2, variable=burger_var)
btn_burger3 = Radiobutton(root, text="Chickenburger", value=3, variable=burger_var)
btn_burger1.select() #default selection 

btn_burger1.pack()
btn_burger2.pack()
btn_burger3.pack()


label2 = Label(root, text="select your drink")
label2.pack()
drink_var = StringVar()
btn_drink1 = Radiobutton(root, text="Coke", value="Coke", variable=drink_var)
btn_drink2 = Radiobutton(root, text="Beer", value="Beer", variable=drink_var)
btn_drink3 = Radiobutton(root, text="TapWater", value="Water", variable=drink_var)
btn_drink3.select()

btn_drink1.pack()
btn_drink2.pack()
btn_drink3.pack()


def btncmd():
    print(burger_var.get()) # get selected radio button value 
    print(drink_var.get()) # get selected radio button value 


btn = Button(root,text= "Click", command=btncmd)
btn.pack()


root.mainloop()