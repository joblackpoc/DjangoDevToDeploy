# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods
name = 'Natthawut'
age = 45
# Concatenate
print('Hello my name is ' + name + ' and I am ' + str(age))
# String Formatting
# Arguments by position
print('{}, {}, {}'.format('a', 'b', 'c'))
print('{1}, {2}, {0}'.format('a', 'b', 'c'))
# Arguments by name
print('My name is {name} and I am {age}'.format(name=name, age=age))
print('My name is {name} and I am {age}'.format(name='POC', age='45'))
# F-Strings (only in python 3.6+)
print(f'My name is {name} and I am {age}')
# String Methods
s = 'hello everybody in the world'
w = 'tO bE nUMBER oNE '
# Capitalize first 
print(s.capitalize())
# Make all uppercase
print(s.upper())
# Make all lower
print(s.lower())
# Swap case -> make it become opposite case
print(w.swapcase())
# Get lenght
print (len(s))
# Replace
print(s.replace('world', 'room'))
# Count
t = 'Natthawut Ponkrut is very good'
sub1 = "u"
sub2 = "o"
print(t.count(sub1))
print(t.count(sub2))
# Starts with
print(t.startswith('N'))
# Ends with
print(t.endswith('d'))
# Split into a list
print(t.split())
# Find position
print(t.find('r'))
# Is all alphanumeric -> check is it alphanumeric
print(t.isalnum())
# Is all alphabetic -> check is it alphabet
print(t.isalpha())
# Is all numeric
print(t.isnumeric())