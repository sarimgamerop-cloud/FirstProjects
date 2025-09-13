from tkinter import *
import tkinter.messagebox as tmsg

def Rate():
    print("Rating!")
    Rate_Show = tmsg.showinfo("Rating!",f"Thanks for your {slider1.get()} Star Rating!")

root =Tk()
root.geometry("500x500")

Label_text = Label(text="How was your experience? Rate us !")
slider1 = Scale(root, from_=1 , to=10 , orient="horizontal" , tickinterval=2)
Label_text.pack()
slider1.pack()
Button_1 = Button(root, text="Rate!" , command=Rate).pack()

root.mainloop()