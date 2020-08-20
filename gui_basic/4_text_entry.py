from tkinter import *

root = Tk()
root.title("My GUI")
root.geometry("640x480")

txt = Text(root, width=30, height=5) #Text 는 여러줄 
txt.pack()
txt.insert(END, "글자를 입력하세요")



e = Entry(root, width=30)  # Entry 는 한줄 
e.pack()
e.insert(0, "please input here ")

def btncmd():
    print(txt.get("1.0", END)) #Grab the text from line 1, and 0 column to END 
    print(e.get())

    #delete 
    txt.delete("1.0", END)
    e.delete(0,END)


btn = Button(root,text= "Click", command=btncmd)
btn.pack()

root.mainloop()