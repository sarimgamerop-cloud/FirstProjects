from tkinter import *
from datetime import datetime
import tkinter.messagebox as tmsg
import ctypes

myappid = 'YourCompany.YourApp.1.0'
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

root = Tk()
root.geometry("400x400")
root.title("CustomerSales")
root.minsize(400, 200)

# Create main frames using grid
header_frame = Frame(root, bg="#32CD32", height=60)
header_frame.grid(row=0, column=0, columnspan=3, sticky="ew")

title_frame = Frame(header_frame, bg="#32CD32")
title_frame.place(relx=0.5, rely=0.5, anchor="center")

subheader_frame = Frame(root, bg="#32CD32", height=25)
subheader_frame.grid(row=1, column=0, columnspan=3, sticky="ew")

form_frame = Frame(root)
form_frame.grid(row=2, column=0, columnspan=3, pady=20)

note_frame = Frame(root, relief=GROOVE, bd=2)
note_frame.grid(row=3, column=0, columnspan=3, padx=10, pady=10, sticky="ew")

status_frame = Frame(root)
status_frame.grid(row=4, column=0, columnspan=3, sticky="ew")

# Configure grid weights for proper resizing
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(2, weight=1)  # Form frame gets extra space
form_frame.grid_columnconfigure(1, weight=1)

# Header
Label(title_frame, text="Customer Service", font="Calibri 14 bold", bg="#32CD32").pack()

# Subheader
Label(subheader_frame, text="Daily Submissions Forms Records", bg="#32CD32").pack(pady=2)

# StringVar variables
Canvas_Entry_Names_var = StringVar()
Canvas_Entry_Price_var = StringVar()
Canvas_Entry_Paid_var = StringVar()
Entry_Height = StringVar()
Entry_width = StringVar()
Color_Canvas_Theme_var = StringVar(value="white")
statusvar = StringVar()

# Form labels and entries using grid
Label(form_frame, text="Product:", font="Aldhabi 9 bold").grid(row=0, column=0, sticky="e", padx=5, pady=5)
Canvas_Entry_Names = Entry(form_frame, textvariable=Canvas_Entry_Names_var, width=25)
Canvas_Entry_Names.grid(row=0, column=1, padx=5, pady=5)

Label(form_frame, text="Price:", font="Aldhabi 9 bold").grid(row=1, column=0, sticky="e", padx=5, pady=5)
Canvas_Entry_Price = Entry(form_frame, textvariable=Canvas_Entry_Price_var, width=25)
Canvas_Entry_Price.grid(row=1, column=1, padx=5, pady=5)

Label(form_frame, text="Amount Paid:", font="Aldhabi 9 bold").grid(row=2, column=0, sticky="e", padx=5, pady=5)
Canvas_Entry_Paid = Entry(form_frame, textvariable=Canvas_Entry_Paid_var, width=25)
Canvas_Entry_Paid.grid(row=2, column=1, padx=5, pady=5)

# Submit button
Button_Submit = Button(form_frame, text="Submit", command=Submit, highlightthickness=2, relief=GROOVE, padx=20)
Button_Submit.grid(row=3, column=0, columnspan=2, pady=10)

# Note section
Label(note_frame, text="Dear Users Your Records will be Saved within your Directory with File", 
      wraplength=380).pack(pady=2)
Label(note_frame, text="Named (CustomerRecords.txt) and can be accessed anytime !").pack(pady=2)

# Status bar
statusvar.set("Sales Program")
Status_Label = Label(status_frame, textvariable=statusvar, relief=GROOVE, anchor='w')
Status_Label.pack(side=BOTTOM, fill="x")

# Functions Defining
def Submit():
    print("Form Submitted")
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
        return
    
    statusvar.set("Saved")  
    now = datetime.now()
    print(f"{Canvas_Entry_Names_var.get(),Canvas_Entry_Price_var.get(),Canvas_Entry_Paid_var.get()}Return:{Due} , TimeDate : {now}")
    tmsg.showinfo("Saving Info ", "Succesfully Saved !")  

    with open("CustomerRecords.txt" , "a") as f:
        f.write(f" Product :{(Canvas_Entry_Names_var.get())}, Price :{(Canvas_Entry_Price_var.get())}, Paid :{(Canvas_Entry_Paid_var.get())} Returned:{Due} , TimeDate : {now}\n ")

    Canvas_Entry_Names_var.set("")
    Canvas_Entry_Price_var.set("")  
    Canvas_Entry_Paid_var.set("")    
    statusvar.set("Saved !")
    Canvas_Entry_Names.focus_set()
    statusvar.set("Ready for new entry")

def Quiting():
    print("Quiting")
    b = tmsg.askquestion("Quit?", "Do You Want To Quit? Unsaved Record will be lost")
    if(b == "yes"):
         root.destroy()

def ShowAbout():
    print("Showing About")
    tmsg.showinfo("About" , "Made By SpecialCodes for Public Purposes And Training")

def TopLevel():
    Toplevel_Options = Toplevel(root)
    Toplevel_Options.title('Resize Options')
    Toplevel_Options.geometry("300x300")
     
    Label(Toplevel_Options, text="---------------------------------------------------------------").pack()
    Label(Toplevel_Options, text="Window Resizer !", font="Raleway 15").pack()
    Label(Toplevel_Options, text="---------------------------------------------------------------").pack()

    Label(Toplevel_Options, text="Height :").pack()
    Height_Entry = Entry(Toplevel_Options, textvariable=Entry_Height)
    Height_Entry.pack()

    Label(Toplevel_Options, text="Width :").pack()
    Width_Entry = Entry(Toplevel_Options, textvariable=Entry_width)
    Width_Entry.pack()

    Label(Toplevel_Options, text="---------------------------------------------------------------").pack()
    
    resize_button = Button(Toplevel_Options, text='Resize!', command=local_resize)
    resize_button.pack()

    Height_Entry.bind("<Return>", lambda e: Width_Entry.focus())
    Width_Entry.bind("<Return>", lambda e: resize_button.focus())

def local_resize():
    print("resizing")
    try:
        width = max(300, min(2000, int(Entry_width.get())))
        height = max(200, min(1500, int(Entry_Height.get())))
        root.geometry(f"{width}x{height}")
        print(f"Resized to: {width}x{height}")
    except ValueError:
        tmsg.showerror("Invalid Input", "Please enter valid numbers for width and height.")

def Appearence_Function():
    print("opening Appearence")
    Appearence_window = Toplevel(root)
    Appearence_window.title("Appearence Theme")
    Appearence_window.geometry("351x345")
    Appearence_window.minsize(351,345)
    Appearence_window.maxsize(351,345)

    Label(Appearence_window, text="---------------------------------------------------------------").pack()
    Label(Appearence_window, text="Appearence", font="Raleway 13").pack()
    Label(Appearence_window, text="---------------------------------------------------------------").pack()
    Label(Appearence_window, text="Enter Your Color", font="Calibri 10").pack()

    Color_Entry = Entry(Appearence_window, textvariable=Color_Canvas_Theme_var)
    Color_Entry.pack()

    Label(Appearence_window, text="---------------------------------------------------------------").pack() 
    Label(Appearence_window, text='*Black Color Isnt Recommended*', font="SmallFonts 8 italic").pack()

    Button(Appearence_window, text='Change!', command=Change_Color, pady=5).pack()

    listbox = Listbox(Appearence_window)
    listbox.pack(side=LEFT, anchor="sw", padx=60, pady=10)
 
    colors = [
        "red", "green", "blue", "yellow", "orange", "purple", "pink", "brown", 
        "black", "white", "gray", "lightblue", "lightgreen", "lightyellow",
        "lightgray", "cyan", "magenta", "silver", "gold", "navy", "maroon", 
        "turquoise", "violet", "coral", "aqua"
    ]
    for color in colors:
        listbox.insert(END, color)
        
    Button(Appearence_window, text="From List", command=From_List_Change).pack(side=LEFT, padx=2)

def Change_Color():
    color = Color_Canvas_Theme_var.get().lower()
    valid_colors = ["red", "green", "blue", "yellow", "orange", "purple", "pink", 
                   "brown", "black", "white", "gray", "lightblue", "lightgreen", 
                   "lightyellow", "lightgray", "cyan", "magenta", "silver", "gold", 
                   "navy", "maroon", "turquoise", "violet", "coral", "aqua"]
    
    if color in valid_colors:
        form_frame.config(bg=color)
        header_frame.config(bg=color)
        subheader_frame.config(bg=color)
    else:
        tmsg.showerror("Invalid Color", "Please enter a valid color name")

def From_List_Change():
    selected_color = listbox.get(ACTIVE)
    Color_Canvas_Theme_var.set(selected_color)
    Change_Color()

# MenuBar
Menu_Bar = Menu(root)
Appearence_Menu = Menu(Menu_Bar, tearoff=0)
Appearence_Menu.add_command(label="Theme", command=Appearence_Function)
Menu_Bar.add_cascade(label="Appearence", menu=Appearence_Menu)

Menu_Submenu = Menu(Menu_Bar, tearoff=0)
Menu_Submenu.add_command(label="Save To Records", command=Submit)
Menu_Submenu.add_command(label="Quit Program", command=Quiting)
Menu_Submenu.add_command(label="About", command=ShowAbout)
Menu_Submenu.add_command(label="Resize", command=TopLevel)
Menu_Bar.add_cascade(label="Options", menu=Menu_Submenu)

root.config(menu=Menu_Bar)

# Key bindings
Canvas_Entry_Names.bind("<Return>", lambda e: Canvas_Entry_Price.focus())
Canvas_Entry_Price.bind("<Return>", lambda e: Canvas_Entry_Paid.focus())
Canvas_Entry_Paid.bind("<Return>", lambda e: Button_Submit.focus())
Button_Submit.bind("<Return>", lambda e: Submit())

root.mainloop()