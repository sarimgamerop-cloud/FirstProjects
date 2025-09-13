import customtkinter as ctk
from PIL import Image

ctk.set_appearance_mode("dark")

root = ctk.CTk()
root.geometry("1000x700")
root.maxsize(1000,700)
root.minsize(1000,700)

frame = ctk.CTkFrame(root,width = 800 ,height = 800 , fg_color="#2c2c2c", border_color="darkgrey", border_width=2 ,corner_radius=15)
frame.pack(side = 'right' , fill='y' , padx =20 , pady =20)
frame.pack_propagate(False)

# Label_text = ctk.CTkLabel(frame , text = " Your Own Expenses App" , font = ("FSP DEMO - Argent CF Light" , 35) )
# Label_text.pack(padx= 10 , pady =10)


pillow_image = Image.open("ei_1757669412955-removebg-preview.png")
Photo_text = ctk.CTkImage(light_image = pillow_image , dark_image = pillow_image , size=(700,200))
Label_Phototext = ctk.CTkLabel(master=frame , image=Photo_text , text="")
Label_Phototext.pack(pady=10)

root.mainloop()