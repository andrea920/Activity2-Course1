class Customers:
    greeting = "Welcome to the Coffee Palace!"

c_1= Customers()
c_1.Name = "Samirah"
c_1.Beverage = "Iced caffe latte"
c_1.Food = "Cinnamon roll"
c_1.Total = 225

c_2= Customers()
c_2.Name = "Jerry"
c_2.Beverage = "Caramel macchiato"
c_2.Food = "Glazed doughnut"
c_2.Total = 230

print(Customers.greeting)
print(c_1.Beverage)
print(c_2.Food)