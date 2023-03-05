# ------------------------------------------------- #
# Title: Assignment 07
# Description: Create a new script that demonstrates how Pickling and Structured error handling work.
# ChangeLog: (Who, When, What)
# VOLaughlin,<3.1.2023>,Created Script
# ------------------------------------------------- #

'''
What's pickling?
Definition: "serializing and deserializing a Python object structure.
In other words, it's the process of converting a Python object into a byte stream to store it in a file/database"
Source: https://www.synopsys.com/blogs/software-security/python-pickling/#:~:text=Pickle%20in%20Python%20is%20primarily,transport%20data%20over%20the%20network.
'''
print("================ Pickling Demo ================")
import pickle  # This imports code from another code file!

# Data -------------------------------------------- #

# First, here's the data that the program must collect from the user. It's stored in a list object.
userId = int(input("Enter an ID: "))
userName = str(input("Enter your name: "))
lstCustomer = [userId, userName]
print(lstCustomer)

# Processing -------------------------------------- #

# Second, the inputted data is stored in a binary file using pickle.dump. It 'dumps' data to a file.
def save_data_to_file(file_name, list_of_data):
    objFile = open(file_name, "ab")
    pickle.dump(list_of_data, objFile)
    objFile.close()

def read_data_from_file(file_name):
    objFile = open("AppData.dat", "rb")
    list_of_data = pickle.load(objFile)
    objFile.close()
    print(list_of_data)

'''Success! You know how to pickle data!'''

print("================ End Pickling Demo ================")


print("============ Error Handling Demo ==============")
'''
What's error handling?
Definition: "Structured exception handling is a mechanism for handling both hardware and software exceptions"
Source: https://learn.microsoft.com/en-us/windows/win32/debug/structured-exception-handling
'''

'''Try-Except error handling'''

# Demo 1: Try-except with a custom error message
try:
    quotient = 5/2 # there will not be an error because 5 is divisible by 2.
    (print(quotient), print("= 5 divided by 2"))
except:
    print("Demo 1: There was an error!") # custom error message
# Demo 2: Try-except with a built-in Python error handling function and a custom error message
try:
    quotient = 5/0
except ZeroDivisionError as e: # built-in Python error handling function
    print("Demo 2: Please do not use Zero for the second number!") # custom error message to go along with it
# Demo 3: Try-except with a different built-in Python error handling function and a custom error message
try:
    quotient = 5/0
except Exception as e: # built-in Python error handling function
    print("Demo 3: You cannot divide a number by 0!") # custom error message to go along with it

''' Raising Custom Errors'''
# Demo 1: Simple raise exception with custom message example
int_fav_number = (int(input("Enter your favorite number: ")))
if not type(int_fav_number) is int:
  raise TypeError("Demo 1: Only integers are allowed")

# Demo 2: Raise exception and try-except working together
try:
    new_file_name = input("Enter the name of the file you want to make: ")
    if new_file_name.isnumeric():
        raise Exception("Error: No numbers allowed in my files!")
except Exception as e:
    print("Error: No numbers allowed in my files!")

print("============ End Error Handling Demo ==============")
