from tkinter import *

root =Tk()
root.geometry("600x600")

def add():
    global i
    print("added")
    listbox.insert(ACTIVE , f"{i}" )
    i+=1
    print(i)


i = 0

scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT , fill=Y)
listbox = Listbox(root , yscrollcommand = scrollbar.set)
listbox.pack()
listbox.insert(END, "First Item")

Button = Button(root, text="ADD TO CART", command=add).pack()
scrollbar.config(command=listbox.yview)


root.mainloop()