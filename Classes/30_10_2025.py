# class Calculator:
#     def __init__(self,a,b):
#         self.a = a
#         self.b = b

#     def add(self):
#         print(self.a + self.b)
#     def subtract(self):
#         print(self.a - self.b)
#     def multiply(self):
#         print(self.a * self.b)
#     def divide(self):
#         try:
#             print(self.a / self.b)
#         except ZeroDivisionError as e:
#             print(e)
# a1 = Calculator(0,0)
# a1.add()
# a1.divide()



# # inheritance concepts
# class Factory:
#     def __init__(self):
#         pass
#     def make_vehicle(self):
#         print("I'm making all vehicles")
    
# class BikeFactory(Factory):
#     def __init__(self):
#         pass
#     def make_car(self):
#         print("I'm bike factory so I can make only bikes")
#     def make_vehicle(self):
#         print("Iam changing my factory to my own")
# factorys = Factory()
# factorys.make_vehicle()


# evening task
# Person and Student
# Create a Person class with attributes name and age.
# Create a subClass Student that inherits from Person  (Hint: use the super keyword in python and use)
# Print all attributes through a new method in Student class.

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age= age

class Student(Person):
    def __init__(self, name, age):
        super().__init__(name,age)

    def show(self):
        print(self.name)
        print(self.age)
data =Student("Yashika",19)
print(data.name,data.age)

# #The Shape System
# Parent Shape (Shape)
# Initialize with a color (string).
# Implement a method `describe()`- print the current color.
# Implement a method area() that do nothing and just pass the method and comes out. 
# Child Shape (Circle)
# Inherit from Shape class
# The initializer must accept color (string) and radius (float).
# Override the area() method to calculate and return the area of the circle (3.14 * r * r).
# Create a Circle object. Call both describe() and area() and print the results.
# Demonstrate what happens if you try to instantiate Shape and call its area().

# class Shape:
#     def __init__(self,color):
#         self.color = color

#     def describe(self):
#         print(self.color)
#     def area()
    




        