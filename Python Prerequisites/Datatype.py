# datatype are the type which tell us about the type of data we are using 

''' 
Numeric - int, float, complex
Sequence Type - string, list, tuple
Mapping Type - dict
Boolean - bool
Set Type - set, frozenset
Binary Types - bytes, bytearray, memoryview

'''

a = 5
print(type(a))

b = 5.0
print(type(b))

c = 2 + 4j

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


