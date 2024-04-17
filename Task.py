#Kepp entering number until number is between 1 to 10\
    
# while(True):   #1
#     print("Enter number")   
#     n= int(input())     #43 
#     if(n>=1 and n<=10): #43>=1 and 43<=10 wrong ,so loop me nahi jaye ga 
#         print("You entered ",n)
#         break
    

# print number in reverse order till 1

# print("Enter number")
# number =int(input())
# for i in range(number,0,-1):# hero 0 is not included   , inization, conditon,inc/dec
    
#     if(i==5):
#         break
#     print(i)
 


# functions

# 01 - square of a number 
# def square_of_a_number(number):
#     square = number ** 2
#     return square

# n = int(input("Enter the number: "))
# print(square_of_a_number(n))

# 02 - create a function that takes 2 nos a parameters
#      and returns their sum

# def addition_of_numbers(a1,a2):
#     sum = a1 + a2 
#     return sum 

# print (addition_of_numbers(1,2))

# 03 - polymorphism

# def multiply(a3,a4):
#     return a3*a4

# print(multiply(5,"aa"))

# 04 - area and circumference of a circle

# import math

# def circle(radius):
#     area = math.pi * radius ** 2
#     circ = 2 * math.pi * radius
#     return area , circ

# y , z = circle(4)      -----
# print("Area is ", y , "circumference is ", z)



# 05 - write a function that greets a user, if 
#      no user name is provided then it should 
#      use a default name 


# def name(n = "Mohit"):
#     return "Hello " + n 

# y = input("Enter your name : ")
# if y == "":
#     print(name())   #------  only function is called
# else:
#     print(name(y))
    
    
# 06 - lambda function (used only when fun is used only once)
#      cube of a number

# cube = lambda x : x ** 3

# print(cube(3))


# 07 - *args

# def sum_all(*args):
#     # sum = 0
#     # for i in args:
#     #     sum = sum + i
#     # return sum
#     return sum(args)
    
# print(sum_all(1, 2, 4))


# 08 - **kwargs
# create a function that accepts any no of keyword
# args and prints them in format key : value


# def print_kwargs(**kwargs):
#     for key,value in kwargs.items():
#        # print(key, ":", value)
#        print(f"{key}: {value}")
        
# print_kwargs(name = "mohit", classs = "10")

# 9 - yield 





# 10 - recursive function to claculate 
#      factorial of a number


# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n - 1)
    
# print(factorial(5))





# object oriented programming

# # 01 -
    
    
    
# class Car:                              
#     def __init__(self,brand,model):
#         self.brand = brand
#         self.model = model
        
# my_car = Car("Toyota",'LC')    # object
# print(my_car.brand)
# print(my_car.model)


# # 02 - CLASS METHOD AND self
# # Add a method to the Car class that displays 
# #the full name of the car(brand and model)

# class Car:
#     def __init__(self,brand,model):
#         self.brand = brand
#         self.model = model
        
#     def full_name(self):
#         return f"{self.brand}{self.model}"
# my_car = Car("hyundai","Exter")
# print(my_car.full_name())


# # 03 - inheritance

# class Car:
#     def __init__(self,brand,model):
#         self.brand = brand
#         self.model = model
    
#     def full_name(self):
#         return f"{self.brand} {self.model}"
    
# class ElectricCar(Car):
#     def __init__(self,brand,model,battery_size):
#         super().__init__(brand,model)
#         self.battery_size = battery_size

# my_car = ElectricCar("Tesla", "model x", "90 kWh")
# print(my_car.full_name())
# print(my_car.brand)



# 04 - Encapsulation

# class Car:
#     def __init__(self,brand,model):
#         self.__brand = brand
#         self.model = model
        
#     def get__brand(self):
#         return self.__brand 
    
# my_car = Car("Tesla", "x")

# print(my_car.get__brand())



# 05 - Polymorphism

class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
    
    def full_name(self):
        return f"{self.brand} {self.model}"
    
    def fuel_type(self):
        return "petrol or Diesel"
    
class ElectricCar(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size
    
    def fuel_type(self):
        return "Electric charge"

my_car = ElectricCar("Tesla", "model x", "90 kWh")
print(my_car.fuel_type())
my_car2 = Car("Tata", "Safari")
print(my_car2.fuel_type())



# 06 - class variable

