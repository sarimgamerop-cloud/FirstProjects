from tkinter import *

root = Tk()
root.geometry("559x445")
root.title("recordkeeping")
root.minsize(559,445)
root.maxsize(559,445)


Label_heading = Label(text="RECORDS", bg ="green", fg = "white",pady=4 ,padx = 235, font ="Raleway 14 bold", borderwidth =2 , relief=SUNKEN)
Label_heading.grid(row=1,column=0)

Label_2 = Label(text="Record Program Made By SPECIALCODES!", bg ="grey", fg = "black", font="SmallFonts 7", padx = 186 , pady= 4)
Label_2.grid()




root.mainloop()