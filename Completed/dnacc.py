from tkinter import *
import pickle
import os
os.system("clear")

root = Tk()
root.geometry("444x444")
root.minsize(300,300)
root.maxsize(500,500)

def Submit():
    print("Form Submitted")
    print(f"{Name_Entry_value.get(),Age_Entry_value.get(),School_Entry_value.get(),Roll_Entry_value.get(),Class_Entry_value.get()}Near?={Checkboxval.get()}")
    

    with open("records.txt" , "a") as f:
        f.write(f"{Name_Entry_value.get(),Age_Entry_value.get(),School_Entry_value.get(),Roll_Entry_value.get(),Class_Entry_value.get(),Checkboxval.get()}\n ")  


def Checksubmit():
    print("residency")


Header = Label(text ="DANCE REGISTRATION", font="Raleway 16", pady =9).grid(column=1)

Name = Label(root, text=" Your Name :" ).grid()  
Age = Label(root, text="Your Age :").grid()
School = Label(root, text="Your School :").grid()
Roll = Label(root, text="Your RollNo :").grid()
Class = Label(root, text="Your Class :").grid()

Name_Entry_value = StringVar()
Age_Entry_value = StringVar()
School_Entry_value = StringVar()
Roll_Entry_value= StringVar()
Class_Entry_value = StringVar()

Name_Entry = Entry(root , textvariable = Name_Entry_value).grid(row=1,column=1)
Age_Entry = Entry(root, textvariable = Age_Entry_value).grid(row=2,column=1)
School_Entry = Entry(root, textvariable = School_Entry_value).grid(row=3,column=1)
Roll_Entry = Entry(root, textvariable = Roll_Entry_value).grid(row=4,column=1)
Class_Entry = Entry(root, textvariable = Class_Entry_value).grid(row=5,column=1)

Checkboxval = IntVar()

Checkbox = Checkbutton(root, text="near resident?".upper(), variable = Checkboxval).grid()

Button(root, text="submit now".upper(), command = Submit).grid(row=7,column=1)




root.mainloop()