from tkinter import *
root =Tk()
Canvas_Hieght = 400
Canvas_Width = 400
root.geometry("400x400")

Can_widget = Canvas(root,width=Canvas_Width, height=Canvas_Hieght)
Can_widget.pack()

Can_widget.create_line(10,10,390,10)
Can_widget.create_line(10,10,10,390)
Can_widget.create_line(10,390,390,390)
Can_widget.create_line(390,10,390,390)

Can_widget.create_oval(20,20,380,380, fill="grey")
Can_widget.create_text(200,200, text="CREATE" , fill ="green", font="Raleway 12")















root.mainloop()
