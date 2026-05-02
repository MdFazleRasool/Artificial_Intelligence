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
 

#String in Python
string = "Hello, World!"

#length of string
print(len(string))

#string concatenation
greeting = "Hello"
name = "Alice"
message = greeting + ", " + name + "!"
print(message)


#String Slicing
string = "Hello, World!"
print(string[0]) #H
print(string[7]) #W
print(string[-1]) #!
print(string[0:5]) #Hello
print(string[7:]) #World!
print(string[:5]) #Hello
print(string[::2]) #Hlo ol!
print(string[::-1]) #!dlroW ,olleH
#String Formatting
a=5
b=10
sum = a + b

#normal formatting with format() method
print("The sum of {} and {} is {}".format(a, b, sum))
print("The sum of {0} and {1} is {2}".format(a, b, sum))
print("The sum of {1} and {0} is {2}".format(a, b, sum))



#f-string formatting
print(f"The sum of {a} and {b} is {sum}")

'''

""" Built-in data types in Python"""
# 1. Numeric types: int, float, complex
# 2. Sequence types: list, tuple, range
# 3. Text type: str
# 4. Mapping type: dict
# 5. Set types: set, frozenset
# 6. Boolean type: bool

# Sequence types: list, tuple, range
# List
my_list = [1, 2, 3, 4, 5]
print(my_list) # [1, 2, 3, 4, 5]
print(my_list[0]) # 1
print(my_list[1:4]) # [2, 3, 4]
my_list.append(6) # add element to the end of the list
print(my_list) # [1, 2, 3, 4, 5, 6]
print(len(my_list)) # 6
my_list.remove(3) # remove element from the list
print(my_list) # [1, 2, 4, 5, 6]

# List slicing
my_list = [1, 2, 3, 4, 5]
print(my_list[0:3]) # [1, 2, 3] 
print(my_list[2:]) # [3, 4, 5]
print(my_list[:3]) # [1, 2, 3]

# Methods of list
my_list = [1, 2, 3, 4, 5]

my_list.append(6) # add element to the end of the list
print(my_list) # [1, 2, 3, 4, 5, 6]

my_list.insert(0, 0) # add element at specific position
print(my_list) # [0, 1, 2, 3, 4, 5, 6]

my_list.remove(3) # remove element from the list
print(my_list) # [0, 1, 2, 4, 5, 6]

my_list.pop() # remove last element from the list
print(my_list) # [0, 1, 2, 4, 5]

my_list.pop(0) # remove element at specific position
print(my_list) # [1, 2, 4, 5]

my_list.sort() # sort the list in ascending order
print(my_list) # [1, 2, 4, 5]  

my_list.sort(reverse=True) # sort the list in descending order
print(my_list) # [5, 4, 2, 1]

my_list.reverse() # reverse the list
print(my_list) # [1, 2, 4, 5]

# Loops in list
my_list = [1, 2, 3, 4, 5]
for i in my_list:
    print(i) # 1 2 3 4 5

find  = 3
idx=0
for i in my_list:
    if i == find:
        print(f"{i} found at index {idx}")
        break
    idx += 1


# Tuples
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple) # (1, 2, 3, 4, 5)
print(type(my_tuple)) # <class 'tuple'>
print(my_tuple[0]) # 1
print(my_tuple[1:4]) # (2, 3, 4)
print(len(my_tuple)) # 5

# Methods of tuple
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple.count(3)) # 1
print(my_tuple.index(3)) # 2

sum = 0
for i in my_tuple:
    sum += i
print(f"The sum of elements in the tuple is: {sum}")

# Occurrences of an element in a tuple
my_tuple = (1, 2, 3, 4, 5, 3, 2, 1)
element = 3
count = 0
for i in my_tuple:
    if i == element:
        count += 1
print(f"The number of occurrences of {element} in the tuple is: {count}")

my_tuple.count(3) # 2
my_tuple.index(3) # 2 (first occurrence of 3 is at index 2) 


# Dictionaries
my_dict = {"name": "Alice", "age": 30, "city": "New York"}
print(my_dict) # {'name': 'Alice', 'age': 30, 'city': 'New York'}
print(my_dict["name"]) # Alice
print(my_dict.get("age")) # 30  
print(type(my_dict)) # <class 'dict'>
"""
1. Unordered collection of key-value pairs
2. Keys must be unique and immutable (string, number, tuple)    
3. Values can be of any data type

"""

#methods of dictionary
my_dict = {"name": "Alice", "age": 30, "city": "New York"}
my_dict_values = list(my_dict.values()) # get values of the dictionary
print(my_dict_values) # ['Alice', 30, 'New York']

my_dict_keys = list(my_dict.keys()) # get keys of the dictionary
print(my_dict_keys) # ['name', 'age', 'city']

my_dict_items = list(my_dict.items()) # get key-value pairs of the dictionary
print(my_dict_items) # [('name', 'Alice'), ('age', 30), ('  city', 'New York')] 

my_dict.get("name") # Alice
my_dict.get("mf") # None


# Sets (Unordered collection of unique elements)
my_set = {1, 2, 3, 4, 5}
print(my_set) # {1, 2, 3, 4, 5}
print(type(my_set)) # <class 'set'>
print(len(my_set)) # 5


"""
 1. Unordered collection of unique elements
 2. Mutable (can be modified after creation)
 3. No duplicate elements allowed
 4. No indexing or slicing (since it's unordered)
 5. Useful for membership testing and eliminating duplicates from a sequence
 6. Set operations: union, intersection, difference, symmetric difference
 7. Methods: add(), remove(), discard(), pop(), clear(), union(), intersection(), difference(), symmetric_difference()
 8. Set comprehension: {expression for item in iterable if condition}
 9. Frozenset: immutable version of a set (cannot be modified after creation)
 10. Frozenset methods: union(), intersection(), difference(), symmetric_difference()   
 11. Frozenset operations: union, intersection, difference, symmetric difference
 12. Frozenset comprehension: frozenset(expression for item in iterable if condition)
 13. Set and frozenset can be used as keys in a dictionary since they are immutable, but they cannot contain mutable elements like lists or dictionaries as their elements.
"""

# Methods of set
my_set = {1, 2, 3, 4, 5}
my_set.add(6) # add element to the set
print(my_set) # {1, 2, 3, 4, 5, 6}

my_set.remove(3) # remove element from the set
print(my_set) # {1, 2, 4, 5, 6

my_set.discard(4) # remove element from the set (does not raise an error if the element is not present)
print(my_set) # {1, 2, 5, 6}

my_set.clear() # remove all elements from the set
print(my_set) # set()

my_set.pop() # remove and return an arbitrary element from the set
print(my_set) # {2, 5, 6} (the output may vary since sets are unordered)    

# Set operations
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
union_set = set1.union(set2) # union of two sets
print(union_set) # {1, 2, 3, 4, 5, 6, 7, 8}

intersection_set = set1.intersection(set2) # intersection of two sets
print(intersection_set) # {4, 5}


difference_set = set1.difference(set2) # difference of two sets
print(difference_set) # {1, 2, 3}

symmetric_difference_set = set1.symmetric_difference(set2) # symmetric difference of two sets
print(symmetric_difference_set) # {1, 2, 3, 6, 7, 8}

# symmetric difference of two sets using operator
symmetric_difference_set = set1 ^ set2
print(symmetric_difference_set) # {1, 2, 3, 6, 7, 8}

"""
  symmetric difference of two sets means the elements that are in either set1 or set2 
  but not in both. In this case, the symmetric difference of set1 and set2 is {1, 2, 3, 6, 7, 8} 
  because these are the elements that are present in either set1 or set2 but not in both sets. 
  The elements 4 and 5 are not included in the symmetric difference because they are present in both sets.
"""

