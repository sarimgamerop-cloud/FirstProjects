from tkinter import *
from datetime import datetime
import tkinter.messagebox as tmsg
import ctypes

myappid = 'YourCompany.YourApp.1.0'  # Can be any unique string
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

root = Tk()
root.geometry("400x400")
root.title("CustomerSales")
# Now using min and max sizes correctly, Can be removed though
root.minsize(400,200)
root.iconbitmap("output-onlinepngtools.ico")

# Add the missing StringVar variables
Entry_Height = StringVar()
Entry_width = StringVar()

# Functions Defining
def resize():
    print("resizing")
    root.geometry(f"{Entry_width.get()}x{Entry_Height.get()}")  # Was out of order

def TopLevel():
    Toplevel_Options = Toplevel(root)
    Toplevel_Options.title('Resize Options')
    Toplevel_Options.geometry("300x300")
     
    Label_3 = Label(Toplevel_Options, text="---------------------------------------------------------------")
    Label_3.pack()

    Label_1 = Label(Toplevel_Options, text="Window Resizer !", font = "Raleway 15")
    Label_1.pack()

    Label_2 = Label(Toplevel_Options, text="---------------------------------------------------------------")
    Label_2.pack()

    Height_Label = Label(Toplevel_Options, text="Height :")
    Height_Label.pack()

    Height_Entry = Entry(Toplevel_Options, textvariable = Entry_Height)
    Height_Entry.pack()

    Width_Label = Label(Toplevel_Options, text="Width :")
    Width_Label.pack()
    
    Width_Entry = Entry(Toplevel_Options, textvariable=Entry_width)
    Width_Entry.pack()

    Label_4 = Label(Toplevel_Options, text="---------------------------------------------------------------")
    Label_4.pack()
    
    resize_button = Button(Toplevel_Options, text = 'Resize!', command = local_resize)  # resize now works
    resize_button.pack()# added resizing checks with exceptions

    Height_Entry.bind("<Return>" , lambda e: Width_Entry.focus())
    Width_Entry.bind("<Return>" , lambda e: resize_button.focus())
    
    
      


def local_resize():
    print("resizing")
    try:
        width = int(Entry_width.get())
        height = int(Entry_Height.get())
        if width > 0 and height > 0:
            root.geometry(f"{width}x{height}")
            print(f"Resized to: {width}x{height}")
        else:
            tmsg.showerror("Invalid Input", "Width and Height must be positive numbers.")
    except ValueError:
        tmsg.showerror("Invalid Input", "Please enter valid numbers for width and height.")

# Submitting and Saving function
def Submit():
    print("Form Submitted")
    global Canvas_Entry_Names_var, Canvas_Entry_Price_var, Canvas_Entry_Paid_var , statusvar
    
        

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
    
    statusvar.set("Saved")  
    now = datetime.now()
    print(f"{Canvas_Entry_Names_var.get(),Canvas_Entry_Price_var.get(),Canvas_Entry_Paid_var.get()}Return:{Due} , TimeDate : {now}")
    Message = tmsg.showinfo("Saving Info ", "Succesfully Saved !")  

    with open("CustomerRecords.txt" , "a") as f:
        f.write(f" Product :{(Canvas_Entry_Names_var.get())}, Price :{(Canvas_Entry_Price_var.get())}, Paid :{(Canvas_Entry_Paid_var.get())} Returned:{Due} , TimeDate : {now}\n ")

    Canvas_Entry_Names_var.set("")  # Clear product entry
    Canvas_Entry_Price_var.set("")   # Clear price entry  
    Canvas_Entry_Paid_var.set("")    # Clear paid entry
    statusvar.set("Saved !")
    if(Canvas_Entry_Names.focus()):
        statusvar.set("SalesProgram")
       
# Quiting Functions
def Quiting():
    print("Quiting")
    b = tmsg.askquestion("Quit?", "Do You Want To Quit? Unsaved Record will be lost")
    if(b == "yes"):
         root.destroy()
    else:
        print("Quit Failed")


# About Menu Functions
def ShowAbout():
    print("Showing About")
    About_Message = tmsg.showinfo("About" , "Made By SpecialCodes for Public Purposes And Training")

# Apperance Menu 

def Appearence_Function():

    global Color_Canvas_Theme_var , listbox

    print("opening Appearence")
    Appearence_window = Toplevel(root)
    Appearence_window.title("Appearence Theme")
    Appearence_window.geometry("351x345")
    Appearence_window.minsize(351,345)
    Appearence_window.maxsize(351,345)

    Label_Senctions = Label(Appearence_window, text="---------------------------------------------------------------")
    Label_Senctions.pack()

    

    Label_Appearence = Label(Appearence_window, text="Appearence", font = "Raleway 13")
    Label_Appearence.pack()

    Label_Senctions = Label(Appearence_window, text="---------------------------------------------------------------")
    Label_Senctions.pack()

    Label_Appearence_2 = Label(Appearence_window, text="Enter Your Color", font = "Calibri 10")
    Label_Appearence_2.pack()


    Color_Entry = Entry(Appearence_window , textvariable=Color_Canvas_Theme_var)
    Color_Entry.pack()

    Label_Senctions = Label(Appearence_window, text="---------------------------------------------------------------")
    Label_Senctions.pack() 

    Note_Label = Label(Appearence_window, text = '*Black Color Isnt Recommended*' , font="SmallFonts 8 italic")
    Note_Label.pack()

    Change = Button(Appearence_window, text = 'Change!', command = Change_Color , pady=5)
    Change.pack()

    listbox = Listbox(Appearence_window)
    listbox.pack(side=LEFT, anchor="sw" , padx=60 , pady=10)
 
    colors = [
    "red", "green", "blue", "yellow", "orange",
    "purple", "pink", "brown", "black", "white",
    "gray", "lightblue", "lightgreen", "lightyellow",
    "lightgray", "cyan", "magenta", "silver", "gold",
    "navy", "maroon", "turquoise", "violet", "coral", "aqua"
    ]
    for color in colors:
        listbox.insert(END, color)
    add_button = Button(Appearence_window, text="From List", command=From_List_Change).pack(side=LEFT , padx =2)




def Change_Color():
    print("Changed Color")
    Canvas_Creation.config(bg=Color_Canvas_Theme_var.get())
    return 


def From_List_Change():
    global listbox
    selected_color = listbox.get(ACTIVE)
    Color_Canvas_Theme_var.set(selected_color)  # Update the StringVar
    Canvas_Creation.config(bg=selected_color)  # Change canvas color  


Color_Canvas_Theme_var = StringVar(value="white")
  # Canvas Creation 
Canvas_Creation = Canvas(root , bg =Color_Canvas_Theme_var.get())
Canvas_Creation.pack(fill=BOTH , expand=True)

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

Canvas_Entry_Names.bind("<Return>" , lambda e: Canvas_Entry_Price.focus())
Canvas_Entry_Price.bind("<Return>" , lambda e: Canvas_Entry_Paid.focus())
Canvas_Entry_Paid.bind("<Return>" , lambda e: Button_Submit.focus())
Button_Submit.bind("<Return>" , lambda e: Submit())


# MenuBar
Menu_Bar = Menu(root)
Appearence_Menu = Menu(Menu_Bar , tearoff =0)
Appearence_Menu.add_command(label="Theme" , command=Appearence_Function)
Menu_Bar.add_cascade(label="Appearence" , menu=Appearence_Menu)
Appearence_Menu = Menu(Menu_Bar , tearoff =2)
Appearence_Menu.add_command(label="Theme")
root.config(menu=Menu_Bar)
Menu_Submenu = Menu(Menu_Bar , tearoff =0)
Menu_Submenu.add_command(label="Save To Records", command=Submit)
Menu_Submenu.add_command(label="Quit Program", command=Quiting)
Menu_Submenu.add_command(label="About", command=ShowAbout)
Menu_Submenu.add_command(label="Resize", command=TopLevel)
Menu_Bar.add_cascade(label="Options", menu=Menu_Submenu)

# Lower Note Rectangle :
Canvas_Creation.create_rectangle(10,250,390,290, width=2)
Canvas_Creation.create_text(200,260, text="Dear Users Your Records will be Saved within your Directory with File")
Canvas_Creation.create_text(200,273, text="Named (CustomerRecords.txt) and can be accessed anytime !")

statusvar = StringVar()
statusvar.set("Sales Program")
Status_Label = Label(root , textvariable=statusvar, relief = GROOVE , anchor ='w' )
Status_Label.pack(side=BOTTOM , fill="x")

root.mainloop()