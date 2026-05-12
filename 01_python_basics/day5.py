# File  I/O
# 1. Open a file    
# 2. Read/Write to the file
# 3. Close the file
'''
# Write to a file
file = open('file.txt', 'w')  # 'w' for write mode
file.write('Hello, World!\n')  # Write a line to the file   
file.write('Welcome to Python programming.\n')  # Write another line to the file
file.close()  # Close the file


# Open a file
file = open('file.txt', 'r')  # 'r' for read mode
data = file.read()  # Read the contents of the file
print(data)  # Print the contents of the file
print(type(data))  # Print the type of data (should be str)
file.close()  # Close the file

# readlines() method reads the file and returns a list of lines
file = open('file.txt', 'r')
lines = file.readlines()  # Read the lines of the file into a list
print(lines)  # Print the list of lines
print(type(lines))  # Print the type of lines (should be list)  
file.close()  # Close the file




#With Keyword :-
# The with statement automatically closes the file after the block of code is executed
with open('file.txt', 'r') as file:  # Open the file in read mode
    data = file.read()  # Read the contents of the file
    print(data)  # Print the contents of the file   
with open('file.txt', 'w') as file:  # Open the file in write mode
    file.write('This is a new line.\n')  # Write a new line to the file
    file.write('This will overwrite the previous content.\n')  # Write another line to the file


#delete a file
import os
os.remove('file.txt')  # Remove the file named 'file.txt'

#append to a file
with open('file.txt', 'a') as file:  # Open the file in append
    file.write('This line will be appended to the file.\n')  # Write a line to the file
    file.write('This will not overwrite the existing content.\n')  # Write another line to the file

#file Operations
'''
'''
 r - Read mode (default): Opens a file for reading. The file pointer is placed at the beginning of the file. If the file does not exist, it raises an error.
 w - Write mode: Opens a file for writing. If the file already exists, it truncates the file to zero length (i.e., deletes the existing content). If the file does not exist, it creates a new file.
 a - Append mode: Opens a file for appending. The file pointer is placed at the end of the file. If the file does not exist, it creates a new file.
 r+ - Read and write mode: Opens a file for both reading and writing. The file pointer is placed at the beginning of the file. If the file does not exist, it raises an error.
 w+ - Write and read mode: Opens a file for both writing and reading. If the file already exists, it truncates the file to zero length. If the file does not exist, it creates a new file.  
 a+ - Append and read mode: Opens a file for both appending and reading. The file pointer is placed at the end of the file. If the file does not exist, it creates a new file.
 x - Exclusive creation mode: Opens a file for exclusive creation. If the file already exists, it raises an error. If the file does not exist, it creates a new file.   
 b - Binary mode: This is not a standalone mode but can be combined with other modes (e.g., 'rb' for reading a binary file, 'wb' for writing a binary file). It indicates that the file should be treated as a binary file rather than a text file. 
 t - Text mode (default): This is the default mode for opening files. It indicates that the file should be treated as a text file. When you read from a file in text mode, it returns a string. When you write to a file in text mode, it expects a string. 
 (+) - Update mode: This is not a standalone mode but can be combined with other modes (e.g., 'r+' for reading and writing, 'w+' for writing and reading). It allows you to read and write to the file. The behavior of the file pointer depends on the base mode (e.g., 'r+' starts at the beginning, while 'w+' truncates the file). 



#Word search in a file
word = input("Enter a word to search in the file: ")  # Get the word
with open('file.txt', 'r') as file:  # Open the file in read mode
    data = file.read()  # Read the contents of the file
    if word in data:  # Check if the word is in the file
        print(f"The word '{word}' is found in the file.")  # Print if the word is found
    else:
        print(f"The word '{word}' is not found in the file.")  # Print if the word is not found



# Exception Handling :- 

Definition: Exception handling is a programming construct that allows developers to handle and manage errors or exceptional conditions that may occur during the execution of a program. 
It provides a way to gracefully handle errors without crashing the program.
In Python, exception handling is done using the try-except block. 
The code that may raise   an exception is placed inside the try block, and the code to handle the exception is placed inside the except block. 
If an exception occurs in the try block, the program will jump to the except block and execute the code there. If no exception occurs, the except block is skipped.    




try:
    num1 = int(input("Enter the first number: "))  # Get the first number from the user
    num2 = int(input("Enter the second number: "))  # Get the second number from the user
    result = num1 / num2  # Perform division
    print(f"The result of {num1} divided by {num2} is: {result}")  # Print the result   
except ZeroDivisionError:  # Handle division by zero error
    print("Error: You cannot divide by zero.")  # Print an error message for division by zero
except ValueError:  # Handle invalid input error
    print("Error: Please enter valid integers.")  # Print an error message for invalid input
else:
    print("Division performed successfully.")  # Print a success message if no exceptions occur 
finally:
    print("This block will always be executed.")  # Print a message that will always be executed regardless of exceptions



# List Comprehension with Exception Handling
numbers = [10, 20, 0, 30, 'a', 40]  # A list of numbers with some invalid entries
results = []  # An empty list to store results
for num in numbers:  # Iterate through each number in the list
    try:
        result = 100 / num  # Attempt to divide 100 by the number
        results.append(result)  # Append the result to the results list
    except ZeroDivisionError:  # Handle division by zero error
        print(f"Error: Cannot divide by zero for number {num}.")  # Print an error message for division by zero
    except TypeError:  # Handle invalid type error
        print(f"Error: Invalid type for number {num}.")  # Print an error message for invalid type      
print("Results of division:", results)  # Print the results of the division operations


nums = [-1, 0, -5, 10, 20]  # A list of numbers with some negative and zero values
nums = [0 if num < 0 else num for num in nums]  # Replace negative numbers with zero using list comprehension
print(nums)  # Print the modified list of numbers

'''

words = ['hello', 'world', 'python', 'programming']  # A list of words
print([word.upper() for word in words])  # Convert each word to uppercase using list comprehension and print the result 

result = [val.upper() for val in words]  # Convert each word to uppercase using list comprehension and store the result in a new list
print(result)  # Print the new list of uppercase words


