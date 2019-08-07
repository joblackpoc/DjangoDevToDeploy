# A List is a collection which is ordered and changeable. Allows duplicate members.
# Create list
numbers = [1,2,3,4,5,6,7,8,9]
print(type(numbers))
print(numbers)
# Using a constructor
num = list((1,2,3,4,5,6,7,8,9))
fruits = ['Apples', 'Oranges', 'Grapes', 'Pears']
print(num)
print(fruits)
# Get value
print(fruits[3])
# Get len
print(len(fruits))
# Append to list
fruits.append('Mangoes')
print(fruits)
# Remove from list
fruits.remove('Pears')
print(fruits)
# Insert into position
fruits.insert(4, 'Strawberries')
print(fruits)
# Remove from position
fruits.pop(1)
print(fruits)
# Reverse list
fruits.reverse()
print(fruits)
# Sort list
fruits.sort()
print(fruits)
# Reverse list
fruits.sort(reverse=True)
print(fruits)