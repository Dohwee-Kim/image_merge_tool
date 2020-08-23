import tkinter.ttk as ttk
from tkinter import *
import time


root = Tk()
root.title("my GUI")
root.geometry("640x480")

#progressbar = ttk.Progressbar(root, maximum= 100, mode="indeterminate")
#progressbar = ttk.Progressbar(root, maximum= 100, mode="determinate")

#milli sec 
#progressbar.start(10)  #move per 10 millisec
#progressbar.pack()

p_var2 = DoubleVar()  #percentage may not be integer type
progressbar2 = ttk.Progressbar(root, maximum=100, length=150, variable=p_var2)
progressbar2.pack()

def btncmd2():
    for i in range (101):
        time.sleep(0.01) # 0.01 sec delay
        p_var2.set(i)
        progressbar2.update()   # screen update refresh

btn2 = Button(root, text="Start", command = btncmd2)
btn2.pack()

#def btncmd():
#    progressbar.stop()

#btn = Button(root, text="Stop", command = btncmd)
#btn.pack()
root.mainloop()