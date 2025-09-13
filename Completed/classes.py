# class Car:
#     def __init__(self , brand , year):
#         self.brand = brand
#         self.year = year

    

    
#     # def __repr__(self):
#     #    return f"Car(CarBrand = {self.brand} and Year = {self.year})"

#     def info(self , current_year):
#         return f"This is a {self.brand} from {self.year} with a age of {self.age(current_year)} "

#     def age(self , current_year):
#         return current_year  - self.year

        

# car1 = Car("Toyota" , 1903)
# car2  = Car("Mehran" , 1907)

# print(car1.info(2025))
# print(car2.info(2025))


import tkinter as tk

root = tk.Tk()
root.geometry("400x400")


Label = tk.Label( text="-------------------------------------------------------------------------")
Label.pack()
Expenses_Entry_Product = tk.Entry(root)
Expenses_Entry_Product.pack()
Label = tk.Label( text="-------------------------------------------------------------------------")
Label.pack()
Expenses_Entry_Price = tk.Entry(root)
Expenses_Entry_Price.pack()

class Expense:
    def __init__(self , Item , Price ):
        self.Item = Item
        self.Price = Price

    
    def info(self):
        return f"You Bought {self.Item} of cost {self.Price}"

 Expenses = Expense(Expenses_Entry_Product , Expenses_Entry_Price)
 if Expenses_Entry_Product == price

# e2 = Expense("Bread" , 200)
# e3 = Expense("Egg" , 120)

# e_list = [e1 , e2 , e3]

# for exp in e_list:
#     print(exp.info())


root.mainloop()