print(" Started Learning Python!")
print("Welcome to Day 1 of the coding challenge!")

# variables
name = "Alice"  
age = 30
print("Name:", name)
print("Age:", age)

#Python is a Case Sensitive Language

# Data Types

# Integer (+ve , -ve, 0)
number = 10 
print("Number:", number)

# String    
text = "Hello, World!"
print("Text:", text)
print("Data type of text:", type(text))
# Float (Decimal numbers)
pi = 3.14   
print("Pi:", pi)
print("Data type of pi:", type(pi)) 

# Boolean (True or False)
is_sunny = True
print("Is it sunny?", is_sunny)
print("Data type of is_sunny:", type(is_sunny))



# None (Represents the absence of a value)
nothing = None
print("Nothing:", nothing)
print("Data type of nothing:", type(nothing))

#Comments
# This is a single-line comment 
"""
    This is a multi-line comment 
    It can span multiple lines
    Useful for longer explanations or documentation
"""

# Style Guide
# Use meaningful variable names
first_name = "Alice"
# Use snake_case for variable names
last_name = "Smith"
# Use spaces around operators
full_name = first_name + " " + last_name
print("Full Name:", full_name)
print("Data type of full_name:", type(full_name))

#Program

# Sum of two numbers
num1 = 5
num2 = 10
sum = num1 + num2
print("Sum of", num1, "and", num2, "is:", sum)


#Operators
# Arithmetic Operators (+ , - , * , / , % , ** , //)
# % Modulus operator gives the remainder of a division

num1 = 10
num2 = 3    
print(num1, "Sum", num2, "is:", num1 + num2)
print(num1, "Difference", num2, "is:", num1 - num2)
print(num1, "Product", num2, "is:", num1 * num2)        
print(num1, "Quotient", num2, "is:", num1 / num2)
print(num1, "Remainder", num2, "is:", num1 % num2)
print(num1, "Exponentiation", num2, "is:", num1 ** num2)
print(num1, "Floor Division", num2, "is:", num1 // num2)    

# Comparison Operators (== , != , > , < , >= , <=)
a = 5

b = 10
print(a, "is equal to", b, ":", a == b)
print(a, "is not equal to", b, ":", a != b)         
print(a, "is greater than", b, ":", a > b)
print(a, "is less than", b, ":", a < b)
print(a, "is greater than or equal to", b, ":", a >= b)
print(a, "is less than or equal to", b, ":", a <= b)

# Assignment Operators (= , += , -= , *= , /= , %= , **= , //=)
x = 5   
print("Initial value of x:", x)
x += 3
print("After x += 3, x is:", x)
x -= 2
print("After x -= 2, x is:", x)
x *= 4
print("After x *= 4, x is:", x)
x /= 2
print("After x /= 2, x is:", x)
x %= 3
print("After x %= 3, x is:", x)
x **= 2
print("After x **= 2, x is:", x)
x //= 2
print("After x //= 2, x is:", x)

# Logical Operators (and , or , not)
is_raining = True
is_windy = False
print("Is it raining and windy?", is_raining and is_windy)
print("Is it raining or windy?", is_raining or is_windy)
print("Is it not raining?", not is_raining)

# Operators Precedence
"""
1. Parentheses ()
2. Exponentiation **
3. Multiplication *, Division /, Modulus %
4. Addition +, Subtraction -
5. Comparison Operators ==, !=, >, <, >=, <=
6. Logical Operators not, and, or
"""
# Same precedence operators are evaluated from left to right
result = 3 + 4 * 2 / (1 - 5) ** 2
print("Result of the expression is:", result)

# Type Conversion
# 1 . Implicit Type Conversion (Type Coercion)  
    # Python automatically converts one data type to another when necessary

# 2 . Explicit Type Conversion (Type Casting)
# We can manually convert one data type to another using built-in functions 

ans1 = 10 + 3.5 # Implicit type conversion (int to float)
ans2 = int(5+10.5) # Explicit type conversion (float to int)
print("Result of implicit type conversion:", ans1)
print("Result of explicit type conversion:", ans2)


# Input and Output

#String Input
a = input("Enter a number: ") # Input is always treated as a string
print("You entered:", a)
print("Data type of a:", type(a))

# To convert the input to an integer
b = int(input("Enter another number: "))
print("You entered:", b)
print("Data type of b:", type(b))

c = float(input("Enter a decimal number: "))
print("You entered:", c)
print("Data type of c:", type(c))


# WAP to calculate the area avge of 3 numbers
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))
average = (num1 + num2 + num3) / 3
print("The average of the three numbers is:", average)  



#Assignment
 # q1 . Write a program that asks the user for their name and age, then prints asentence like: Hello Shradha, you are 21 years old!
name = input("Enter your name: ")
age = int(input("Enter your age : "))
print(f"Hello {name} , you are {age} years old")

 #Q2. Take two numbers as input from the user and print their sum, difference, product, and quotient.
num1 = int(input("Enter 1st Number : "))
num2 = int(input("Enter 2nd Number : "))
print("Sum:", num1 + num2)
print("Difference:", num1 - num2)
print("Product:", num1 * num2)
print("Quotient:", num1 / num2)

#Q3. Ask the user to enter two integers and one float. Convert them all to floats and print their average

num1 = int(input("Enter 1st integer number: "))
num2 = int(input("Enter 2nd integer number: "))
num3 = float(input("Enter a float number: "))

# Convert all numbers to floats
num1 = float(num1)
num2 = float(num2)
num3 = float(num3)

# Calculate and print the average
average = (num1 + num2 + num3) / 3
print("The average of the three numbers is:", average)

# Q4. Q4. The user enters a string containing a number (e.g., ). Convert it to:

"""
• an integer
• a float
• a string again
Print all three values with their types.
"""
var1 = input("Enter a string containing a number (e.g., 56 ) ")

var1 = int(var1)
print("Integer value:", var1, "Data type:", type(var1))
var1 = float(var1)
print("Float value:", var1, "Data type:", type(var1))
var1 = str(var1)
print("String value:", var1, "Data type:", type(var1))

x = 10 + 3 * 2 ** 2
print("Result of the expression is:", x)

# Q5. Write a program to swap values of two numbers entered by the user
num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))
# Swapping using a temporary variable
temp = num1
num1 = num2
num2 = temp
print("After swapping:")
print("1st number:", num1)
print("2nd number:", num2)

