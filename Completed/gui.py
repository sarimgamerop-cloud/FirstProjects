from tkinter import *

root = Tk()

root.geometry("444x444")
root.minsize(300,300)
root.maxsize(500,500)
root.title("Gui")

Text1 = ("TOP UPCOMING MOVIES")
Label_text = Label(text=Text1, bg = "red", fg ="white" , font="Raleway 12 bold", padx = 444, borderwidth=3 , relief = SUNKEN)
Label_text.pack(side = TOP)

Label2 = Label(text="Rated By IMDB", bg = "green",fg="black",padx= 444 , font = "SmallFonts 9 bold", borderwidth=2 , relief= SUNKEN )
Label2.pack(side=TOP)

image = PhotoImage(file="logo.png")


Label4 = Label(image=image)
Label4.pack(side = TOP)

Label4 = Label(root,text="",bg ="red",fg ="black",pady =180, padx =5, borderwidth=2,relief=SUNKEN)
Label4.pack(side = LEFT , fill=Y)
Label3 = Label(root,text="",bg ="red",fg ="black",pady =180, padx =5, borderwidth=2,relief=SUNKEN)
Label3.pack(side = RIGHT , fill=Y)








root.mainloop()