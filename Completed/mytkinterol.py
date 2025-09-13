from tkinter import *

special_root = Tk()

special_root.title("NEWSPAPER")
special_root.geometry("500x400")
special_root.maxsize(500,400)

def hello():
    print("tkinter button")
    return hello

special_Label_Head = Label(text="Great Times", padx = 500 , pady = 12, bg ="grey",fg="white",borderwidth =5,relief=GROOVE,font="Raleway 16 bold")
special_Label_Head.pack(side="top",fill=X)

special_Label_date = Label(text="Date = 01 September 2025", padx = 500 , pady = 1, bg ="lightgrey",fg="black",borderwidth =5,relief=GROOVE,font="SmallFonts 9 bold")
special_Label_date.pack(side="top",fill=X)

special_Label_subheader = Label(text=" NEWS This day :".upper(), padx = 7 , pady = 1, bg ="grey",fg="black",borderwidth =5,relief=GROOVE,font="SmallFonts 9 bold")
special_Label_subheader.pack(side="left",anchor = "nw",fill=X)

special_Label_end = Label(text=" Follow For More ".upper(), padx = 70 , pady = 10, bg ="grey",fg="black",borderwidth =5,relief=GROOVE,font="Raleway 9 bold")
special_Label_end.pack(side="left",anchor = "sw")

frame = Frame(special_root, borderwidth = 3 , bg ="white", relief =SUNKEN)
frame.pack(side =BOTTOM)

b1 = Button(frame, text ="click me", fg = "black" , command = hello)
b1.pack(side =BOTTOM ,anchor ="se")



















special_root.mainloop()