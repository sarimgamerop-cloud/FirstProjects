from tkinter import *

root = Tk()
root.title('WINDOW RESIZER')
root.geometry("300x300")
def resize():
    print("resizing")
    root.geometry(f"{Entry_hieght.get()}x{Entry_width.get()}")



Label_3 = Label(text="---------------------------------------------------------------")
Label_3.pack(fill=X)

Label_1 = Label(root, text="Window Resizer !", font = "Raleway 15")
Label_1.pack(fill=X)

Label_2 = Label(text="---------------------------------------------------------------")
Label_2.pack(fill=X)

Hieght_Label = Label(root , text="Hieght :")
Hieght_Label.pack(fill=X)
Entry_hieght = StringVar()
Hieght_Entry = Entry(root , textvariable = Entry_hieght)
Hieght_Entry.pack()


Width_Label = Label(root , text="Width :")
Width_Label.pack(fill=X)
Entry_width = StringVar()
Width_Entry = Entry(root , textvariable=Entry_width)
Width_Entry.pack()

Label_4 = Label(text="---------------------------------------------------------------")
Label_4.pack(fill=X)


Button = Button(root, text = 'Resize!', command = resize)
Button.pack()


root.mainloop()