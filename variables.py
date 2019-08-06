# A variable is a container for a value, which can be of various types

'''
This is a 
multiline comment
or docstring (used to define a functions purpose)
can be single or double quotes
'''

"""
VARIABLE RULES:
  - Variable names are case sensitive (name and NAME are different variables)
  - Must start with a letter or an underscore
  - Can have numbers but can not start with one
"""
# Single assignment
x = 1
y = 2.5
name = 'Brad'
is_cool = True
print(x, y, name, is_cool)
# Multiple assignment
x, y, name, is_cool = (1, 2.5, 'Brad', True)
print(x, y, name, is_cool)
# Basic math
a = x + y
b = x - y
print(a, ', ', b)
# Check type
print('type of "a" is ',type(a))
# Casting
x = str(x)
y = int(y)
z = float(y)
print(type(z))
print(z)
