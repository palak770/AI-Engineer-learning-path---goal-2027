# Variable are used to store data values.
# In Python, variables do not need explicit declaration to reserve memory space.
# The declaration happens automatically when a value is assigned to a variable.
# Variables can change type dynamically, meaning you can assign a value of one type to a variable and then later assign a value of another type.    
# This flexibility allows for dynamic typing, which is a key feature of Python.

# Variable 'x' stores the integer value 10
x = 5

# Variable 'name' stores the string "Samantha"
name = "Samantha"  

print(x)
print(name)

# Variable 'l' stores a list of integers and a float
l = [1, 2, 3, 4.5]
print(l)

# Variable 'd' stores a dictionary with string keys and mixed value types
d = {"name": "Alice", "age": 30, "is_student": False}
print(d)

# Variable 'is_active' stores a boolean value
is_active = True
print(is_active)

# Variable 'pi' stores a float value
pi = 3.14
print(pi)

# Variable 'c' stores a complex number
c = 2 + 3j
print(c)

# Variable 's' stores a string
s = "Hello, World!"
print(s)

# Variable 't' stores a tuple of mixed types
t = (1, "two", 3.0, True)
print(t)

# Variable 'set_example' stores a set of integers
set_example = {1, 2, 3, 4}
print(set_example)

# Variable 'b' stores a float value
b = 5.0
print(type(b))  # <class 'float'>

''' 
Variable Naming Rules:
1. Variable names must start with a letter (a-z, A-Z) or an underscore
2. The rest of the variable name can contain letters, digits (0-9), and underscores.
3. Variable names are case-sensitive (e.g., 'age' and 'Age' are different variables).
4. Variable names cannot be a reserved keyword in Python (e.g., 'class', 'def', 'if', etc.).
Valid variable names:
age = 21
_colour = "lilac"
total_score = 90

Invalid variable names:

1name = "Error"  # Starts with a digit
class = 10       # 'class' is a reserved keyword
user-name = "Doe"  # Contains a hyphen


'''

# Multiple variable assignment
x, y, z = 1, 2.5, "Python"
print(x, y, z)   

#type casting 
# it means the data type of a variable in python is converted to another type.


# Converting integer to float
x = 10
y = float(x)
print(y)  # 10.0

# Converting float to integer
y = 10.5
x = int(y)
print(x)  # 10
print(is_active)  # True
print(type(is_active))  # <class 'bool'>

# Converting string to integer
s = "123"
x = int(s)
print(x)  # 123

# Converting string to float
s = "123.45"
x = float(s)
print(x)  # 123.45

# Converting integer to string
x = 100
s = str(x)
print(s)  # "100"

# Converting float to string
s = 3.14
x = str(s)
print(x)  # "3.14"

# Converting list to tuple
l = [1, 2, 3]
t = tuple(l)
print(t)  # (1, 2, 3)

# Converting tuple to list
t = (1, 2, 3)
l = list(t)
print(l)  # [1, 2, 3]

# Converting list to set
l = [1, 2, 2, 3]
s = set(l)
print(s)  # {1, 2, 3}

# Converting set to list
s = {1, 2, 3}
l = list(s)
print(l)  # [1, 2, 3]

# Converting dictionary keys to list
d = {"a": 1, "b": 2}
keys_list = list(d.keys())
print(keys_list)  # ['a', 'b']

# Converting dictionary values to list
values_list = list(d.values())
print(values_list)  # [1, 2]

# Converting dictionary to list of tuples (key-value pairs)
items_list = list(d.items())
print(items_list)  # [('a', 1), ('b', 2)]

# Converting string to list of characters
s = "Hello"
char_list = list(s)
print(char_list)  # ['H', 'e', 'l', 'l', 'o']

# Converting string to set of characters
char_set = set(s)
print(char_set)  # {'H', 'e', 'l', 'o'}

# delete variable using del keyword
del x
# delete variable 'name'
del name

# Swapping of two number 
a = 5
b = 10
a, b = b, a
print(a)  # 10
print(b)  # 5

# Swapping of two variables using a temporary variable
temp = a
a = b
b = temp
print(a)  # 5
print(b)  # 10

# Swapping of two variables using arithmetic operations
a = 5
b = 10
a = a + b  # a becomes 15
b = a - b  # b becomes 5
a = a - b  # a becomes 10
print(a)  # 10
print(b)  # 5

''' Scope of variables
 
 Global variable
 
 Defined outside functions, accessible throughout the program.
To modify within a function, use the global keyword.
Persist in memory for the program’s duration, useful for shared data.

local variable 

Defined within a function or block, accessible only inside that scope.
Destroyed once the function/block ends.
Temporary, used for short-term data.
'''

# Example of global variable
global_var = "I am global"
def global_example():
    global global_var
    global_var = "I am modified globally"
    print(global_var)
    
global_example()  # Output: I am modified globally
# Example of local variable
def local_example():
    local_var = "I am local"
    print(local_var)
local_example()  # Output: I am local
# print(local_var)  # This would raise an error because local_var is not accessible outside the function


# Example of variable scope
def scope_example():
    local_var = "I am local to this function"
    print(local_var)
scope_example()  # Output: I am local to this function
# print(local_var)  # This would raise an error because local_var is not accessible outside the function


# Example of variable shadowing
x = 10  # Global variable
def shadow_example():
    x = 5  # Local variable, shadows the global variable
    print("Local x:", x)  # Output: Local x: 5
shadow_example()  # Output: Local x: 5
print("Global x:", x)  # Output: Global x: 10


# Example of nonlocal variable
def outer_function():
    nonlocal_var = "I am nonlocal"
    def inner_function():
        nonlocal nonlocal_var
        nonlocal_var = "I am modified in inner function"
        print(nonlocal_var)
    inner_function()  # Output: I am modified in inner function
    print(nonlocal_var)  # Output: I am modified in inner function
outer_function()  # Output: I am modified in inner function


# Example of variable type change
def type_change_example():
    var = 10  # Initially an integer
    print("Initial type:", type(var))  # Output: <class 'int'>
    var = "Now I am a string"  # Change to string
    print("Changed type:", type(var))  # Output: <class 'str'>
type_change_example()  # Output: Initial type: <class 'int'>, Changed type: <class 'str'>


# Example of variable reassignment
def reassignment_example():
    var = 5  # Initially an integer
    print("Before reassignment:", var)  # Output: Before reassignment: 5
    var = "Reassigned to a string"  # Reassign to a string
    print("After reassignment:", var)  # Output: After reassignment: Reassigned to a string
reassignment_example()  # Output: Before reassignment: 5, After reassignment: Reassigned to a string


# Example of variable deletion
def deletion_example():
    var = "I will be deleted"
    print("Before deletion:", var)  # Output: Before deletion: I will be deleted
    del var  # Delete the variable
    # print(var)  # This would raise an error because var is deleted
d = {"name": "Alice", "age": 30, "is_student": False}
print(d)  # Output: {'name': 'Alice', 'age': 30,
# 'is_student': False}

# Example of variable in a loop
def loop_variable_example():
    for i in range(3):
        loop_var = i * 2
        print("Loop variable:", loop_var)  # Output: Loop variable: 0, 2, 4
    # print(loop_var)  # This would raise an error because loop_var is not accessible outside the loop
loop_variable_example()  # Output: Loop variable: 0, 2, 4   

# Example of variable in a conditional statement
def conditional_variable_example():
    if True:
        conditional_var = "I am true"
        print("Conditional variable:", conditional_var)  # Output: Conditional variable: I am true
    # print(conditional_var)  # This would raise an error because conditional_var is not accessible outside the if block
conditional_variable_example()  # Output: Conditional variable: I am true

# Example of variable in a class
class VariableExample:
    def __init__(self):
        self.class_var = "I am a class variable"
    
    def display(self):
        print(self.class_var)
example = VariableExample()
example.display()  # Output: I am a class variable

# Example of variable in a function with default argument
def default_argument_example(arg="Default Value"):
    print("Argument value:", arg)  # Output: Argument value: Default Value
default_argument_example()  # Output: Argument value: Default Value

# Example of variable in a function with variable-length arguments
def variable_length_example(*args):
    print("Variable-length arguments:", args)  # Output: Variable-length arguments: (1, 2, 3)
variable_length_example(1, 2, 3)  # Output: Variable-length arguments: (1, 2, 3)

# Example of variable in a function with keyword arguments
def keyword_argument_example(**kwargs):
    print("Keyword arguments:", kwargs)  # Output: Keyword arguments: {'name': 'Alice', 'age': 30}
keyword_argument_example(name="Alice", age=30)  # Output: Keyword arguments: {'name': 'Alice', 'age': 30}

# Example of variable in a function with both positional and keyword arguments
def mixed_arguments_example(pos_arg, *args, **kwargs):
    print("Positional argument:", pos_arg)  # Output: Positional argument: 1
    print("Variable-length arguments:", args)  # Output: Variable-length arguments: (2, 3)
    print("Keyword arguments:", kwargs)  # Output: Keyword arguments: {'name': 'Alice'}
mixed_arguments_example(1, 2, 3, name="Alice")  # Output: Positional argument: 1, Variable-length arguments: (2, 3), Keyword arguments: {'name': 'Alice'}

# Define 'ba' as a bytearray before using it
ba = bytearray([1, 2, 3, 4, 5])
print(ba)  # Output: bytearray(b'\x01\x02\x03\x04\x05')
print(type(ba))  # <class 'bytearray'>
print(ba[0])  # 1
print(ba[1])  # 2
print(ba[2])  # 3
print(ba[3])  # 4
print(ba[4])  # 5
print(ba[-1]) # 5

# Type conversion
#it means the process of converting a variable from one data type to another.

# Converting bytearray to bytes
ba_bytes = bytes(ba)
print(ba_bytes)  # Output: b'\x01\x02\x03\x04\x05'
print(type(ba_bytes))  # <class 'bytes'>

# Converting bytes to bytearray
b_bytes = bytes([1, 2, 3, 4, 5])
ba_from_bytes = bytearray(b_bytes)
print(ba_from_bytes)  # Output: bytearray(b'\x01\x02\x03\x04\x05')

