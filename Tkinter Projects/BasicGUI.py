from tkinter import *

root = Tk()
root.title("BasicGUI")
root.geometry("400x400")

Label = Label(text="Hello" , bg = "#EDC9AF").grid(row=6)

Canvas_Creation = Canvas(root, height=400 , width = 400, bg ="#EDC9AF")
Canvas_Creation.grid()

Canvas_Creation.create_oval(340,0,410,85, fill = "purple")
Canvas_Creation.create_oval(355,75,390,110, fill = "purple")
Canvas_Creation.create_oval(-3,0,60,85, fill ="purple")

Canvas_Creation.create_rectangle(10,10,390,60 , fill="#32CD32" , width = 2)



Canvas_Creation.create_text(200,35, text="< SPECIALCODES >" , font="Raleway 14" , fill="black" )

Canvas_Creation.create_rectangle(10,65,390,85,fill="#FFD700",outline = "black", width =2)
Canvas_Creation.create_text(200,75, text="How To Create These GUI's" , font="SmallFonts 8")



root.mainloop()