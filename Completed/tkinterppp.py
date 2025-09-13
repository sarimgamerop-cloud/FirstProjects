from tkinter import *
from PIL import Image, ImageTk


tkinter_root = Tk()
tkinter_root.title("Microsoft Windows")

tkinter_root.geometry("800x600")
tkinter_root.minsize(700,500)
tkinter_root.maxsize(1000,800)

tkinter_root_Label = Label(text="Microsoft Windows".upper(),fg = "black",padx = 500,pady = 20, font =("Raleway", 12 ,"bold"), borderwidth = 2,relief=SUNKEN)
tkinter_root_Label.pack()

image = PhotoImage(file="logo.png")
tkinter_root_Label_Photo = Label(image=image)
tkinter_root_Label_Photo.pack(side="bottom",anchor="nw",fill=X)








tkinter_root.mainloop()