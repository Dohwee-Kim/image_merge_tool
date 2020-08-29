from tkinter import *

root = Tk()
root.title("My GUI")
root.geometry("640x480")

Label(root, text="Please select Menu").pack(side="top")

frame_burger = Frame(root, relief="solid", bd =1)
frame_burger.pack(side="left", fill="both", expand = True)
frame_burger.pack()

Button(frame_burger, text= "Hamburger").pack()
Button(frame_burger, text= "Cheeseburger").pack()
Button(frame_burger, text= "Vegiburger").pack()


frame_drink = LabelFrame(root, text="Drinks")
frame_drink.pack(side="right",fill="both", expand=True)
frame_drink.pack()
Button(frame_drink, text= "Cheeseburger").pack()
Button(frame_drink, text= "Vegiburger").pack()



root.mainloop()
 