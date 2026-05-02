'''
# Conditional Statements in Python
age = int(input("Enter your age: "))
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")   

 
color = input("Enter  color: ")
if color == "red":
    print("Stop the car.")
elif color == "yellow":
    print("Get ready to move.")
elif color == "green":
    print("Go!")
else:
    print("Invalid color.")

age = int(input("Enter your age: "))
if (age < 13):
    print("You are a child.")
elif (age >= 13 and age < 18):
    print("You are a teenager.")
else:
    print("You are an adult.")

# Odd or Even
number = int(input("Enter a number: "))
if number % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")

# Multiple of a number or not
num = int(input("Enter a number: "))
if num % 5 == 0:
    print("The number is a multiple of 5.")
else:
    print("The number is not a multiple of 5.")


# Match Case
color = input("Enter a color: ")
match color:
    case "red":
        print("Stop the car.")
    case "yellow":
        print("Get ready to move.")
    case "green":
        print("Go!")
    case _:
        print("Invalid color.")

# loops

# While loop
count = 0 #iterator
while count < 5:
    print("Count:", count)
    count += 1

# For loop
for i in range(5): #range(start, stop, step)
    print("Iteration:", i)
    
# Multiplication table of a number
num = int(input("Enter a number to display its multiplication table: "))
print(f"Multiplication table of {num}:")
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

# break and continue

for i in range(10):
    if i == 5:
        break
    print("Iteration:", i)

for i in range(10):
    if i == 5:
        continue
    print("Iteration:", i)

# odd numbers from 1 to 20
print("Odd numbers from 1 to 20:")
for i in range(1, 21):
    if i % 2 != 0:
        print(i)

# odd numbers from 1 to 11
print("Odd numbers from 1 to 11:")
for i in range(1, 11,2):
    print(i)


#Vowel count in a string
string = input("Enter a string: ")
vowels = "aeiouAEIOU"
count=0
for char in string:
    if char in vowels:
        count+=1
print(f"The number of vowels in the string is: {count}")


# Range Function (start, stop, step) 
# (default start is 0 and default step is 1)

for i in range(1, 11, 2): 
    print(i)

# Sum of first n natural numbers
n = int(input("Enter a number: "))  
sum=0
for i in range(1,n+1):
    sum+=i
print(f"The sum of first {n} natural numbers is: {sum}")
# Sum of first n natural numbers using formula
n = int(input("Enter a number: "))
sum = n*(n+1)//2
print(f"The sum of first {n} natural numbers is: {sum}")



""" Functions in Python"""
# block of code which performs a specific task

def greet(name): #function definition
    print(f"Hello, {name}!")

greet("Alice") #function call
greet("Bob")


def add(a, b):
    return a + b
result = add(5, 3)
print("The sum is:", result)

# calculate average

def average(numbers):
    total = sum(numbers)
    count = len(numbers)
    return total / count
nums = [10, 20, 30, 40, 50]
avg = average(nums)
print("The average is:", avg)

# default parameters
def greet(name="Guest"):
    print(f"Hello, {name}!")
greet() # uses default parameter
greet("Alice") # overrides default parameter


"""Types of Functions in Python"""

# 1. Built-in functions
print("Hello, World!") # built-in function

# 2. User-defined functions
def square(x):
    return x * x
print(square(5)) # user-defined function
'''
# 3. Anonymous functions (lambda functions)
add = lambda a, b: a + b
print(add(5, 3)) # lambda function

sub = lambda a ,b: a-b
print(sub(5,3))

""" lambda functions are used for small, one-time operations where a full function definition is not necessary. They are often used in conjunction with functions like map(), filter(), and reduce().
    Syntax: lambda arguments: expression
    lamda parameters: expression (this will get evaluated and returned when the lambda function is called )
"""

#   Factorial of a number 
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1) 
num = int(input("Enter a number to find its factorial: "))
print(f"The factorial of {num} is: {factorial(num)}")   
