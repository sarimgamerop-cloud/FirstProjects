from tkinter import *

def Submit():
    print(PassEntry.get())
    print(ConfirmEntry.get())

root =Tk()
root.geometry("444x444")

Password = Label(root, text="Password")
Confirm = Label(root, text="Confirm")
Password.grid()
Confirm.grid(row=1)

PassEntry = Entry(root, textvariable = Password)
ConfirmEntry = Entry(root, textvariable = Confirm)
PassEntry.grid(row=0,column=1)
ConfirmEntry.grid(row=1,column=1)

Button(text="Submit", command=Submit).grid(row=3,column=1)


root.mainloop()