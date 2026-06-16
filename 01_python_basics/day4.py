#Pillars of OOP
#1. Encapsulation
#2. Inheritance
#3. Polymorphism
#4. Abstraction


#1. Encapsulation: Encapsulation is the concept of Wrapping data (attributes) and methods (functions) into a single unit (class),thereby hiding the internal details and only exposing the necessary functionality.
class Student:
    def __init__(self, name, age):
        # The self parameter is a reference to the current instance of the class. It is used to access the attributes and methods of the class within its own definition.
        self.name = name #Public
        self._age = age  #Protected (conventionally, a single underscore indicates that the attribute is intended for internal use and should not be accessed directly from outside the class)
        self.__grade = "A"  #Private (conventionally, a double underscore indicates that the attribute is intended to be private and should not be accessed directly from outside the class)    

    def display_info(self):
        print(f"Name: {self.name}, Age: {self._age}, Grade: {self.__grade}")
    #getter and setter methods
    def get_grade(self):
        return self.__grade
    def set_grade(self, grade):
        self.__grade = grade
    
# Creating an object of the Student class
student1 = Student("Alice", 20)
student1.display_info()  # Output: Name: Alice, Age: 20, Grade: A
# In this example, we have defined a class called Student with an __init__ method to initialize the attributes name and age.
# We also have a method called display_info to print the student's information.
# We then create an object of the Student class, student1, and call the display_info method to display the student's information.

student1._age = 25  # Modifying the age attribute directly (not recommended)
student1.display_info()  # Output: Name: Alice, Age: 25, Grade: A

student1.set_grade("B")  # Modifying the grade attribute using the setter method
print(student1.get_grade())  # Output: B

student1.__grade = "C"  # Attempting to modify the private attribute directly (not recommended)
print(student1.get_grade())  # Output: B (the private attribute is not modified)


#2. Inheritance: Inheritance is a fundamental principle of object-oriented programming that allows a new class (called a child or subclass) to inherit properties and behaviors (attributes and methods) from an existing class (called a parent or superclass).
class Employee:
    start_time = "9:00 AM"
    end_time = "5:00 PM"

class Manager(Employee):
    def __init__(self):
        super().__init__()  # Call the constructor of the parent class (Employee)
        self.name = "Manager"    
    def display_work_hours(self):
        print(f"Work hours: {self.start_time} to {self.end_time}")

class Developer(Employee):
    def __init__(self):
        super().__init__()  # Call the constructor of the parent class (Employee)
        self.name = "Developer"    
    def display_work_hours(self):
        print(f"Work hours: {self.start_time} to {self.end_time}") 

manager1 = Manager()
print(manager1.name)  # Output: Manager
manager1.display_work_hours()  # Output: Work hours: 9:00 AM to 5:00 PM

developer1 = Developer()
print(developer1.name)  # Output: Developer
developer1.display_work_hours()  # Output: Work hours: 9:00 AM to 5:00 PM
# In this example, we have defined a parent class called Employee with attributes start_time and end_time.
# We then define a child class called Manager that inherits from the Employee class. The Manager class has its own constructor that calls the constructor of the Employee class using super().__init__() to initialize the inherited attributes.
# The Manager class also has its own method called display_work_hours to display the work hours.    

#Type of Inheritance
#1. Single Inheritance: A child class inherits from a single parent class.  
class Parent: # type: ignore
    def parent_method(self):
        print("This is the parent method.")
class Child(Parent): # type: ignore
    def child_method(self):
        print("This is the child method.")
child1 = Child()
child1.parent_method()  # Output: This is the parent method.
child1.child_method()   # Output: This is the child method.

#2. Multiple Inheritance: A child class inherits from multiple parent classes.
class Parent1: # pyright: ignore[reportRedeclaration]
    def method1(self):
        print("This is method 1 from Parent1.") 
class Parent2: # type: ignore
    def method2(self):
        print("This is method 2 from Parent2.")
class Child1(Parent1, Parent2): # pyright: ignore[reportRedeclaration]
    def child_method(self):
        print("This is the child method.")
child1 = Child1()
child1.method1()  # Output: This is method 1 from Parent1.
child1.method2()  # Output: This is method 2 from Parent2.
child1.child_method()  # Output: This is the child method.

#3. Multilevel Inheritance: A child class inherits from a parent class, which in
class Grandparent:
    def grandparent_method(self):
        print("This is the grandparent method.")
class ParentLevel(Grandparent):
    def parent_method(self):
        print("This is the parent method.")

class Child5(ParentLevel):
    def child_method(self):
        print("This is the child method.")
child1 = Child5()
child1.grandparent_method()  # Output: This is the grandparent method.

child1.parent_method()  # Output: This is the parent method.
child1.child_method()  # Output: This is the child method.  


#4. Hierarchical Inheritance: Multiple child classes inherit from a single parent class.
class Parent3:

    def parent_method(self):
        print("This is the parent method.")
class Child3(Parent3):
    def child1_method(self):
        print("This is the child1 method.")
class Child4(Parent3):
    def child2_method(self):
        print("This is the child2 method.")
child1 = Child4()

child1.parent_method()  # Output: This is the parent method.
#child1.child1_method()  # Output: This is the child1 method.
child2 = Child4()
child2.parent_method()  # Output: This is the parent method.    
child2.child2_method()  # Output: This is the child2 method.

#5. Hybrid Inheritance: A combination of two or more types of inheritance.
class Parent1:
    def method1(self):
        print("This is method 1 from Parent1.")
class Parent2:
    def method2(self):
        print("This is method 2 from Parent2.")
class Child1(Parent1):
    def child1_method(self):
        print("This is the child1 method.")
class Child2(Parent1, Parent2):
    def child2_method(self):
        print("This is the child2 method.")
child1 = Child1()
child1.method1()  # Output: This is method 1 from Parent1.
child1.child1_method()  # Output: This is the child1 method.
child2 = Child2()
child2.method1()  # Output: This is method 1 from Parent1.
child2.method2()  # Output: This is method 2 from Parent2.
child2.child2_method()  # Output: This is the child2 method.

#Abstraction:- 
'''Abstraction is the process of hiding the internal details and complexity of an object and exposing only the necessary features and functionalities to the outside world. It allows us to focus on what an object does rather than how it does it.
--> In Python, we can achieve abstraction using abstract classes and abstract methods. 
An abstract class is a   class that cannot be instantiated and is meant to be subclassed. 
An abstract method is a method that is declared in an abstract class but does not have an implementation. 
Subclasses of the abstract class are required to provide an implementation for the abstract method.      
'''

from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius ** 2  
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
circle = Circle(5)
print(f"Area of the circle: {circle.area()}")  # Output: Area of the circle: 78.5
rectangle = Rectangle(4, 6)
print(f"Area of the rectangle: {rectangle.area()}")  # Output: Area of the rectangle: 24


#Polymorphism:- 
'''Polymorphism is the ability of an object to take on many forms. It allows us to use a single interface to represent different types of objects.  
In Python, we can achieve polymorphism through method overriding and operator overloading.
Method overriding occurs when a subclass provides a specific implementation of a method that is already defined in its parent class. The subclass's method overrides the parent class's method, allowing us to call the method on an instance of the subclass and get a different behavior than when calling it on an instance of the parent class.'''
class Animal:
    def sound(self):
        return "Some sound"
class Dog(Animal):
    def sound(self):
        return "Woof"
class Cat(Animal):
    def sound(self):
        return "Meow"
animals = [Dog(), Cat()]
for animal in animals:
    print(animal.sound())
# In this example, we have a parent class called Animal with a method sound. The Dog and Cat classes inherit from the Animal class and override the sound method to provide their specific implementations. When we create instances of Dog and Cat and call the sound method, we get different outputs based on the type of animal, demonstrating polymorphism.

#Type of Polymorphism
#1. function overriding
class Parent:
    def method(self):
        print("This is the parent method.")
class Child(Parent):
    def method(self):
        print("This is the child method.")
child1 = Child()
child1.method()  # Output: This is the child method.
#2.  duck typing
class Bird:
    def fly(self):
        print("The bird is flying.")
class Airplane:
    def fly(self):
        print("The airplane is flying.")
def make_it_fly(flyable):
    flyable.fly()
bird = Bird()
airplane = Airplane()
make_it_fly(bird)  # Output: The bird is flying.
make_it_fly(airplane)  # Output: The airplane is flying.
 