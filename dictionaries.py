# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.

# Simple dict
person = {
  'first_name' : 'John',
  'last_name' : 'Doe',
  'age' : 40,
  'idcard' : 3860100085144
}
print(person)

# Use a constructor
person2 = dict(first_name='John', last_name='Doe', age='40', idcard='3860100085144')
print(person2)
# Access value
print(person['first_name'])
print(person.get('last_name'))
# Add key/value
person['phone'] = '083-502-6598'
print(person)
# Get keys
print(person.keys())
# Get items
print(person.items())
# Make copy
person3 = person.copy()
person3['city'] = 'Chumphon'
print(person3)
# Remove item
del(person['idcard'])
print(person)
# Clear
person.clear
print()
# Get lenght
print(len(person3))
# List of dict
people = [
  {'name': 'Natthawut', 'age': 40},
  {'name': 'Jeeradate', 'age': 37},
  {'name': 'Piyarat', 'age': 32}
]
print(people[0]['name'])
print(people)