from tkinter import *
from datetime import datetime
import tkinter.messagebox as tmsg


root = Tk()
root.geometry("400x400")
root.title("CustomerSales")
root.maxsize(400,400)
root.minsize(400,400)

# Functions Defining

def Submit():
    print("Form Submitted")
    global Canvas_Entry_Names_var, Canvas_Entry_Price_var, Canvas_Entry_Paid_var
    if Canvas_Entry_Paid_var.get() == "" or Canvas_Entry_Price_var.get() == "":
        tmsg.showerror("Invalid Input", "Please Enter Product Price Values")
        return
    try:
        paid = int(Canvas_Entry_Paid_var.get())
        price = int(Canvas_Entry_Price_var.get())
    except ValueError:
        tmsg.showerror("Invalid Input", "Please enter valid numbers for Price and Amount Paid.")
        return
    Due = paid - price
    if paid < price:
        tmsg.showerror("Invalid Input", "Paid amount is less than price. Please enter valid values.")
        print("Please Enter Valid Values")
        return
    now = datetime.now()
    print(f"{Canvas_Entry_Names_var.get(),Canvas_Entry_Price_var.get(),Canvas_Entry_Paid_var.get()}Return:{Due} , TimeDate : {now}")
    Message = tmsg.showinfo("Saving Info ", "Succesfully Saved !")  

    with open("CustomerRecords.txt" , "a") as f:
        f.write(f"{Canvas_Entry_Names_var.get(),Canvas_Entry_Price_var.get(),Canvas_Entry_Paid_var.get()} Returned:{Due} , TimeDate : {now}\n ")
       

def Quiting():
    print("Quiting")
    b = tmsg.askquestion("Quit?", "Do You Want To Quit? Unsaved Record will be lost")
    if(b == "yes"):
         root.destroy()
    else:
        print("Quit Failed")

def ShowAbout():
    print("Showing About")
    About_Message = tmsg.showinfo("About" , "Made By SpecialCodes for Public Purposes And Training")


# Canvas Creation 
Canvas_Creation = Canvas(root, height=400,width=400 , bg = "#EDC9AF")
Canvas_Creation.pack()

# TODO: Creating Designs
Canvas_Creation.create_rectangle(400,0,350,50, fill = "#32CD32", width=2)
Canvas_Creation.create_rectangle(0,0,50,50, fill="#32CD32", width=2)
Canvas_Creation.create_line(50,0,10,10, width=2)
Canvas_Creation.create_line(350,0,390,10,width=2)

# TODO: Creating Designs For Lower Rectangle
Canvas_Creation.create_rectangle(0,63,13,85, fill = "#32CD32", width =2)
Canvas_Creation.create_rectangle(400,63,387,85,fill = "#32CD32" , width=2)

Canvas_Creation.create_rectangle(10,10,390,60, fill = "#32CD32", width =2)
Canvas_Creation.create_text(200,35, text ="Customer Service" , font ="Calibri 14 bold" , fill ="black")

Canvas_Creation.create_rectangle(10,65,390,90, fill="#32CD32",width=2)
Canvas_Creation.create_text(200,77, text="Daily Submissions Forms Records")

# Names Entries

Canvas_Creation.create_text(120,130, text="Product :" , font="Aldhabi 9 bold")
Canvas_Entry_Names_var = StringVar()
Canvas_Entry_Names = Entry(Canvas_Creation, textvariable=Canvas_Entry_Names_var)
Window_Entry = Canvas_Creation.create_window( 220,130, window=Canvas_Entry_Names)

# Price Entry 

Canvas_Creation.create_text(120,155, text=" Price :" , font="Aldhabi 9 bold")
Canvas_Entry_Price_var = StringVar()
Canvas_Entry_Price = Entry(Canvas_Creation, textvariable=Canvas_Entry_Price_var)
Window_Entry = Canvas_Creation.create_window( 220,155, window=Canvas_Entry_Price)

# Paid Amount

Canvas_Creation.create_text(113,180, text="Amount Paid :" , font="Aldhabi 9 bold")
Canvas_Entry_Paid_var = StringVar()
Canvas_Entry_Paid = Entry(Canvas_Creation, textvariable=Canvas_Entry_Paid_var)
Window_Entry = Canvas_Creation.create_window( 220,180, window=Canvas_Entry_Paid)

# Button Submit

Button_Submit = Button(root , text=" Submit ", command=Submit , highlightthickness=2 , relief=GROOVE , padx=20)
Window_Button = Canvas_Creation.create_window(220, 215, window=Button_Submit)

# MenuBar

Menu_Bar = Menu(root)
root.config(menu=Menu_Bar)
Menu_Submenu = Menu(Menu_Bar , tearoff =0)
Menu_Submenu.add_command(label="Save To Records", command=Submit)
Menu_Submenu.add_command(label="Quit Program", command=Quiting)
Menu_Submenu.add_command(label="About", command=ShowAbout)
Menu_Bar.add_cascade(label="Options", menu=Menu_Submenu)

# Lower NOte Rectangle :
Canvas_Creation.create_rectangle(10,250,390,290, width=2)
Canvas_Creation.create_text(200,260, text="Dear Users Your Records will be Saved within your Directory with File")
Canvas_Creation.create_text(200,273, text="Named (CustomerRecords.txt) and can be accessed anytime !")



root.mainloop()

# Hey Aaalluuu here
