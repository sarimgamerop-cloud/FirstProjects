from tkinter import *

root =Tk()

root.geometry("444x444")
root.maxsize(444,444)
root.minsize(444,444)

def hello():
    print("hello")
    return hello

def hi():
    print("hi")
    return hi 

def nihao():
    print("nihao")
    return nihao

def salam():
    print("salam")
    return salam       

frame = Frame(root, borderwidth = 5 , bg ="white", relief =SUNKEN)
frame.pack(side =LEFT, anchor = "nw")

b1 = Button(frame, text ="hello", fg = "black", command=hello)
b1.pack()

b2 = Button(frame, text ="hi", fg = "black", command = hi)
b2.pack()

b3 = Button(frame, text ="nihao", fg = "black", command = nihao)
b3.pack()

b4 = Button(frame, text ="salam", fg = "black", command = salam)
b4.pack()




root.mainloop()