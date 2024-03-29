# If/ Else conditions are used to decide to do something based on something being true or false
w = 20
x = 10
y = 6 
z = 10
# Comparison Operators (==, !=, >, <, >=, <=) - Used to compare values

# Simple if
if x == z:
  print(f'{x} is equal to {z}')
# If else
if x > y:
  print(f'{x} is greater than {y}')
else:
  print(f'{x} is less than {y}')

# elif
if x > y:
  print(f'{x} is greater than {y}')
elif x == y:
  print(f'{x} is equal to {y}')
else:
  print(f'{x} is less than {y}')

# Nested if
if x > 2:
  if x <= 10:
    print(f'{x} is less than 10 and greater than 2')

# Logical operators (and, or, not) - Used to combine conditional statements

# and
if x > 2 and x <= 10:
  print(f'{x} is greater than 2 and less than 10 ')

# or
if x > 2 or x <= 10:
  print(f'{x} is greater than 2 or less than 10')

# not
if not( x == y):
  print(f'{x} is not equal to {y}')


# Membership Operators (not, not in) - Membership operators are used to test if a sequence is presented in an object

# in
numbers = [1,2,3,4,5,6,7,8,9,10]

if x in numbers:
  print(f'{x} in numbers' )
  print(x in numbers)

if w not in numbers:
  print(f'{w} not in numbers')
  print(w not in numbers)

# Identity Operators (is, is not) - Compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:

# is
if x is z:
  print(x is z) 

# is not
if x is not y:
  print(x is not y)  