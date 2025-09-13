from tkinter import *
from PIL import Image, ImageTk

# base of the tkinter
basicgui_root = Tk()
#Title
basicgui_root.title("hello")

# Label options
 #text - 
#bd - background
#fg- foreground
#font- font change font = ("fontname", size e.g 19 , "bold""italic etc")
#padx - 
#pady -
#relief - border stylings SUNKEN,GROOVE,RAISED,RIDGE borderwidth = size

# PAck options
# anchor = "nw""ne" etc
# side = top , bottom , left , right side=bottom


# Size of the gui tkinter WidthxHieght ;
basicgui_root.geometry("1024x1024")

basicgui_root.minsize(1024,1024) # for setting a locked amount of minimization
#(Width,Hieght)
basicgui_root.maxsize(1024,1024) #for setting a locked amount of maximization

# Labeling ( non interactable )

#   basicgui_Label = Label(text="basic gui label is here".upper())

# to show it we need to pack it up

   # basicgui_Label.pack()

# Creating Photos :

 # Image = PhotoImage(file="logo.png")

# In Jpg format by Pillow:

 # Image = Image.open("1.jpg")
 # photo = ImageTk.PhotoImage(Image)



# Create a label for photo
 # basicgui_label_photo = Label(image=Image)
# now pack
  # basicgui_label_photo.pack()


# basic loop
basicgui_root.mainloop()