from tkinter import *
import pickle
import os
os.system("clear")


root = Tk()
root.geometry("444x444")
root.minsize(300,300)
root.maxsize(500,500)

Label(text="Dance Registration".upper(), bg="grey", fg="white", padx =170,pady=5, borderwidth=2, relief = SUNKEN,font="Gibson 13 ").grid(row =0,column=0)

Label2 = Label(text="Please submit your form to participate".upper(),font="Calibri 12 bold", bg="lightgrey" , borderwidth=2,relief=SUNKEN, padx = 170 , pady =3).grid()

Label3 = Label(text=" Submit Here : ".upper(), bg = "grey", font="Gibson 10 ",fg ="white", borderwidth =2 , relief =SUNKEN).grid()

Label4 = Label(root,text=" Name : ".upper(), font="Gibson 10 ", borderwidth =2 , relief =SUNKEN).grid(row=9,column=6)


root.mainloop()