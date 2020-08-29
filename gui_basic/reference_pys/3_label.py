from tkinter import *

root = Tk()
root.title("My GUI")
root.geometry("800x800")


label1 = Label(root, text="Hello")
label1.pack()


photo = PhotoImage(file="gui_basic/bp_jisoo.png")
label2 = Label(root, image=photo)
label2.pack()

def change():
    #label1.config(text="~~ chu")

    #이미지를 바꾸려면 전역변수 선언 
    global photo2
    photo2 = PhotoImage(file="gui_basic/bp_jisoo2.png")
    label2.config(image=photo2)


btn = Button(root,text="Click", command=change)
btn.pack()

root.mainloop()