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
list_frame.pack(fill="both")
scrollbar = Scrollbar(list_frame)
scrollbar.pack(side="right", fill="y")

list_file = Listbox(list_frame, selectmode="extended", height=15, yscrollcommand=scrollbar.set) #max 15 files 
list_file.pack(side="left", fill="both", expand=True)
scrollbar.config(command=list_file.yview)


#save directories 
path_frame = LabelFrame(root, text="Save Folder")
path_frame.pack()
txt_dest_path = Entry(path_frame)
txt_dest_path.pack(side="left", fill = "x", expand = True)

btn_dest_path = Button(path_frame, text="Open", width = 10)
btn_dest_path.pack(side="right")


root.resizable(False,False)
root.mainloop()
