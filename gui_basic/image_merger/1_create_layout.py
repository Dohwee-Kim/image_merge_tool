from tkinter import *

root = Tk()
root.title("Image merging tool ")

#file frame 
file_frame = Frame(root)
file_frame.pack()

btn_add_file = Button(file_frame, text="Add files", padx= 5, pady=5, width=12)
btn_add_file.pack(side="left")

btn_del_file = Button(file_frame, text="Delete files", padx= 5, pady=5, width=12)
btn_del_file.pack(side="right")


#List Frame 
list_frame = Frame(root)
list_frame.pack()
scrollbar = Scrollbar(list_frame)
scrollbar.pack(side="right", fill="y")

list_file = Listbox(list_frame, selectmode="extended", height=15, yscrollcommand=scrollbar.set) #max 15 files 
list_file.pack(side="left", fill="both", expand=True)
scrollbar.config(command=list_file.yview)


root.resizable(False,False)
root.mainloop()
