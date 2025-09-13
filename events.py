from tkinter import *

root = Tk()
root.geometry("400x400")
root.title("SArim Ali".upper())
root.maxsize(400,400)
root.minsize(400,400)

def Sarim(event):
    print(f"You clicked at {event.x} and {event.y} ")

Button = Button(text="click me please")
Button.pack()

root.bind('<Button-1>' , Sarim)

root.mainloop()