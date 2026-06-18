#Class -> Blueprint for creating objects. It defines a set of attributes and methods that the created objects will have.
#Object -> An instance of a class. It is created using the class blueprint and can have its own unique values for the attributes defined in the class.

from symtable import Class


class Student:
    def __init__(self, name, age): #The __init__ method is a special method in Python classes. It is called when an object is created from the class and allows the class to initialize the attributes of the object.
        # self is a reference to the current instance(object) of the class. 
        # It is used to access the attributes and methods of the class within its own definition.
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

# Creating an object of the Student class
student1 = Student("Alice", 20)
student1.display_info()  # Output: Name: Alice, Age: 20
# Creating another object of the Student class
student2 = Student("Bob", 22)
student2.display_info()  # Output: Name: Bob, Age: 22
# In this example, we have defined a class called Student with an __init__ method to initialize the attributes name and age. 
# We also have a method called display_info to print the student's information. 
# We then create two objects of the Student class, student1 and student2, and call the display_info method to display their information.

#types of constructors
#1. Default constructor: A constructor that takes no parameters and initializes the attributes with default values.
class DefaultStudent:
    def __init__(self):
        self.name = "Unknown"
        self.age = 0
default_student = DefaultStudent()
print(default_student.name)  # Output: Unknown

#2. Parameterized constructor: A constructor that takes parameters to initialize the attributes with specific values.
class ParameterizedStudent:
    def __init__(self, name, age):
        self.name = name
        self.age = age
parameterized_student = ParameterizedStudent("Charlie", 25)
print(parameterized_student.name)  # Output: Charlie
#3. Copy constructor: A constructor that creates a new object as a copy of an existing object.
class CopyStudent:
    def __init__(self, student):
        self.name = student.name
        self.age = student.age

original_student = ParameterizedStudent("David", 30)
copy_student = CopyStudent(original_student)
print(copy_student.name)  # Output: David

#Attributes are variables that hold data associated with an object. 
#They represent the state or characteristics of the object.
#Methods are functions defined within a class that describe the behaviors or actions that an object of the class can perform. They can manipulate the attributes of the object or perform specific tasks related to the object.

#Attributes
class Car7:
    #Attribute
    make = "Unknown"
    model = "Unknown"

car1 = Car7()
print(car1.make)  # Output: Unknown

#Methods
class Car1:
    def start_engine(self):
        print("Engine started")
car1 = Car1()
car1.start_engine()  # Output: Engine started

#Types of Methods
#1. Instance Methods: These methods operate on an instance of the class and can access and modify the instance's attributes. They are defined with the first parameter as self, which refers to the instance of the class.
#2. Class Methods: These methods operate on the class itself rather than on instances of the class. They are defined with the @classmethod decorator and take the class as the first parameter, conventionally named cls. Class methods can access and modify class attributes but cannot access instance attributes directly.   
#3. Static Methods: These methods do not operate on an instance or the class itself. They are defined with the @staticmethod decorator and do not take any special first parameter. Static methods are used for utility functions that perform a task in isolation and do not require access to instance or class attributes.   
# Example of Instance Methods, Class Methods, and Static Methods    

#instance Methods 
class Laptop8:
    storage_type = "SSD"  # Class attribute
    def __init__(self, brand, ram):
        self.brand = brand  # Instance attribute
        self.ram = ram      # Instance attribute    
    def display_specs(self):
        print(f"Brand: {self.brand}, RAM: {self.ram}GB, Storage Type: {Laptop8.storage_type}")
laptop1 = Laptop8("Dell", 16)
laptop1.display_specs()  # Output: Brand: Dell, RAM: 16GB

#Class Methods
class Laptop7:
    storage_type = "SSD"  # Class attribute
    def __init__(self, brand, ram):
        self.brand = brand  # Instance attribute
        self.ram = ram      # Instance attribute    
    @classmethod
    def change_storage_type(cls, new_storage_type):
        cls.storage_type = new_storage_type
Laptop7.change_storage_type("HDD")
laptop2 = Laptop8("HP", 8)
laptop2.display_specs()  # Output: Brand: HP, RAM: 8GB, Storage Type: HDD

#Static Methods
# Static methods are defined with the @staticmethod decorator and do not take any special first parameter. 
# Static methods are used for utility functions that perform a task in isolation and do not require access to instance or class attributes.

class Calculator:
    @staticmethod
    def add(a, b):
        return a + b
    @classmethod
    def multiply(cls, a, b):
        return a * b
    # Instance method
    def subtract(self, a, b):
        return a - b
    
# Using static method
result_add = Calculator.add(5, 3)

# Using class method
result_multiply = Calculator.multiply(5, 3)

# Using instance method
calculator = Calculator()
result_subtract = calculator.subtract(5, 3)
print(f"Addition: {result_add}, Multiplication: {result_multiply}, Subtraction: {result_subtract}")

#Product Store

# Design and Create an online store for products (name,price,quantity) and implement the following functionalities:
#1. Track total number of products in the store.
#2. create a static method to calculate discountedon each product based on a %parameter .

class Product:
    total_products = 0  # Class variable to track total number of products

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        Product.total_products += 1  # Increment total products when a new product is created
        #self .count will create a instance variable count for each object created from the Product class, and it will be initialized to 0 for each object.
    
    @classmethod
    def get_total_products(cls):
        return cls.total_products

    @staticmethod
    def calculate_discount(price, discount_percentage):
        discount_amount = price * (discount_percentage / 100)
        discounted_price = price - discount_amount
        return discounted_price
    
# Example usage
product1 = Product("Laptop", 1000, 10)
product2 = Product("Smartphone", 500, 20)
print("Total products in the store:", Product.get_total_products())  # Output: Total products in the store: 2
discounted_price = Product.calculate_discount(product1.price, 10)  # 10% discount
print(f"Discounted price of {product1.name}: ${discounted_price}")  # Output: Discounted price of Laptop: $900.0

