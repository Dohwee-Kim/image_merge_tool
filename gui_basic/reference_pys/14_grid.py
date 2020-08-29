from tkinter import *

root = Tk()
root.title("My GUI")
root.geometry("640x480")


btn1 = Button(root, text="button1")
btn2 = Button(root, text="button2")

#btn1.pack()
#btn2.pack()

#btn1.pack(side="left")
#btn2.pack(side="right")

#btn1.grid(row=0, column=0)
#btn2.grid(row=1, column=1)


#Apple Keyboard layout 

btn_f16 = Button(root, text="F16", padx=10, pady=10)  #expand padding from the center  text 
#btn_f16 = Button(root, text="F16", width=5, height=2)  #fixed width and height 
btn_f17 = Button(root, text="F17")
btn_f18 = Button(root, text="F18")
btn_f19 = Button(root, text="F19")
btn_clear = Button(root, text="clear")
btn_equal = Button(root, text="=")
btn_back_slash = Button(root, text="/")
btn_star = Button(root, text="*")

btn_1 = Button(root, text="1")
btn_2 = Button(root, text="2")
btn_3 = Button(root, text="3")
btn_enter = Button(root, text="Enter")
btn_0 = Button(root, text="0")
btn_comma= Button(root, text=".")



btn_f16.grid(row=0, column=0, sticky=N+E+W+S, padx=3, pady=3)
btn_f17.grid(row=0, column=1, sticky=N+E+W+S)
btn_f18.grid(row=0, column=2, sticky=N+E+W+S)
btn_f19.grid(row=0, column=3, sticky=N+E+W+S)
btn_clear.grid(row=1, column=0, sticky=N+E+W+S)
btn_equal.grid(row=1, column=1, sticky=N+E+W+S)
btn_back_slash.grid(row=1, column=2, sticky=N+E+W+S)
btn_star.grid(row=1, column=3, sticky=N+E+W+S)
btn_1.grid(row=2, column=0, sticky=N+E+W+S)
btn_2.grid(row=2, column=1, sticky=N+E+W+S)
btn_3.grid(row=2, column=2, sticky=N+E+W+S)
btn_enter.grid(row=2, column=3, rowspan=2, sticky=N+E+W+S)
btn_0.grid(row=3, column=0, columnspan=2, sticky=N+E+W+S)
btn_comma.grid(row=3, column=2, sticky=N+E+W+S)



root.mainloop()