# datatype are the type which tell us about the type of data we are using 

''' 
Numeric - int, float, complex
Sequence Type - string, list, tuple
Mapping Type - dict
Boolean - bool
Set Type - set, frozenset
Binary Types - bytes, bytearray, memoryview

'''

#Numeric data type 

a = 5
print(type(a)) # <class 'int'>

b = 5.0
print(type(b)) # <class 'float'>

c = 2 + 4j
print(type(c)) # <class 'complex'>

# Sequence datatype 

'''collection of similar or different data type 
string - immutable sequence of characters
list - mutable sequence of objects
tuple - immutable sequence of objects
'''
# String 

s = "Hello World"
print(type(s)) # <class 'str'>

#access string at index
print(s[0])  # H
print(s[1])  # e
print(s[2])  # l
print(s[-1]) # d

# List 

l = [1, 2, 3, "Hello", 4.5]
print(type(l)) # <class 'list'>
#access list at index
print(l[0])  # 1
print(l[1])  # 2
print(l[2])  # 3
print(l[-1]) # 4.5

# Tuple
t = (1, 2, 3, "Hello", 4.5)
print(type(t)) # <class 'tuple'>
#access tuple at index
print(t[0])  # 1
print(t[1])  # 2
print(t[2])  # 3
print(t[-1]) # 4.5

# Mapping Type - Dictionary
d = {"name": "Alice", "age": 30, "city": "New York"}
print(type(d)) # <class 'dict'>
#access dictionary by key
print(d["name"])  # Alice
print(d["age"])   # 30
print(d["city"])  # New York

# Boolean Type
is_active = True
print(type(is_active)) # <class 'bool'>
is_active = False
print(type(is_active)) # <class 'bool'>

# Set Type
s = {1, 2, 3, "Hello", 4.5}
print(type(s)) # <class 'set'>
#access set (no index, as sets are unordered)
print(1 in s)  # True
print("Hello" in s)  # True

# Frozenset Type
fs = frozenset([1, 2, 3, "Hello", 4.5])
print(type(fs)) # <class 'frozenset'>

# Binary Types
b = bytes([1, 2, 3, 4, 5])
print(type(b)) # <class 'bytes'>
ba = bytearray([1, 2, 3, 4, 5])
print(type(ba)) # <class 'bytearray'>
mv = memoryview(b)
print(type(mv)) # <class 'memoryview'>
# Accessing memoryview
print(mv[0])  # 1
print(mv[1])  # 2
print(mv[2])  # 3
print(mv[-1]) # 5

# End of the code snippet
# Note: Memoryview allows you to access the memory of the bytes object without copying it.
# This is useful for large data processing where performance is critical.
# It provides a way to manipulate the data without creating a new copy, which saves memory and
# processing time.
# This code snippet demonstrates various Python data types and their usage.
# Each data type is printed with its type and some basic operations are shown.






