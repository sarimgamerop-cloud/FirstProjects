from tkinter import *
import tkinter.messagebox as tmsg
root =Tk()
root.geometry("600x600")

def PrintCommand():
    print("WOrks?")

def askquit():
    print("ask quiting")
    value = messagebox.askquestion("Do You Really Want To Quit?" , "Do You Really Want To Quit? ")






 #Menu_1 = Menu(root)
#Menu_1.add_command(label="Print" , command=PrintCommand)
#Menu_1.add_command(label="Quit", command=quit)

#root.config(menu=Menu_1)

MenuBAR = Menu(root)
MenuSubmenu = Menu(MenuBAR , tearoff=0)
MenuSubmenu.add_command(label="Save", command=PrintCommand)
MenuSubmenu.add_command(label="New", command=PrintCommand)
MenuSubmenu.add_separator()
MenuSubmenu.add_command(label="Quit Program", command=askquit)
root.config(menu=MenuBAR)

MenuBAR.add_cascade(label="Options", menu=MenuSubmenu)


slider1 = Scale(root, from_=0 , to=100 , orient=HORIZONTAL ,tickinterval=50)
 # slider1.set(50)
slider1.pack()

root.mainloop()
