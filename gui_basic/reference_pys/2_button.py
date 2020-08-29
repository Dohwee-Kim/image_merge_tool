from tkinter import *

root = Tk()
root.title("My GUI tool")

btn1 = Button(root, text="Button1")
btn1.pack()

btn2 = Button(root, padx=5, pady=10, text="Button22222222222222222")
btn2.pack()

btn3 = Button(root, padx=10, pady=5, text="Button2")  #상대적 설정 
btn3.pack()

btn4 = Button(root, width=10, height=3, text="Button444444444444") #버튼 크기 강제설정 
btn4.pack()

btn5 = Button(root, fg="red", bg="yellow", text="Button5")
btn5.pack()

def btncmd():
    print("I love Jisoo!")

photo = PhotoImage(file="gui_basic/bp_jisoo.png")
btn6 = Button(root, image=photo, command=btncmd)
btn6.pack()



root.mainloop()