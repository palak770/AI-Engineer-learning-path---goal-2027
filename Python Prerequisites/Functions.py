#functions in python 
#function is a block of code that only runs when it is called you can pass data, known as parameters, into a function. A function can return data as a result.
#types of functions
#1. Built-in functions
#2. User-defined functions
#3. Lambda functions
#4. Recursive functions
#5. Higher-order functions
#6. Anonymous functions
#7. Generator functions
#8. Asynchronous functions
#1. Built-in functions
#These are functions that are already defined in Python and can be used directly without any additional code
print(len("Hello, World!"))  # Returns the length of the string
print(max([1, 2, 3, 4, 5]))  # Returns the maximum value in the list
#2. User-defined functions
def greet(name):
    """Function to greet a person."""
    return f"Hello, {name}!"
print(greet("Alice"))  # Calls the user-defined function and prints the greeting
#3. Lambda functions
#These are small anonymous functions defined using the lambda keyword. They can take any number of arguments but can only have one expression.
add = lambda x, y: x + y
print(add(5, 3))  # Calls the lambda function to add two numbers
#4. Recursive functions
#These are functions that call themselves to solve a problem. They are often used for tasks like calculating factorials or Fibonacci numbers.
def factorial(n):
    """Function to calculate the factorial of a number."""
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
print(factorial(5))  # Calls the recursive function to calculate factorial of 5
#5. Higher-order functions
#These are functions that can take other functions as arguments or return a function as a result.
def apply_function(func, value):
    """Function to apply a given function to a value."""
    return func(value)
def square(x):
    """Function to square a number."""
    return x * x
print(apply_function(square, 4))  # Calls the higher-order function to apply square function to 4
#6. Anonymous functions
#These are functions that are defined without a name, often used for short-lived operations.
# They are similar to lambda functions but can be defined using the def keyword without a name.
