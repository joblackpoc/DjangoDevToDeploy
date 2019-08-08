# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
 
# Simple tuple
fruit_tuple = ('Apple', 'Orange', 'Mango', 'Grape')
print(fruit_tuple)
# Get single value
print(fruit_tuple[0])
# Tuples with one value must have trailing comma
fruit_tuple2 = ('Apple',)
print(fruit_tuple2)
# Get lenght of tuple
print(len(fruit_tuple))

# A Set is a collection which is unordered and unindexed. * No duplicate members.*

# Create set
fruit_set = {'Apple', 'Orange', 'Mango', 'Grape', 'Apple'}
print(fruit_set)
# Check if in set
print('Apple' in fruit_set)
# Add to set
fruit_set.add('Banana')
print(fruit_set)
# Remove from set
fruit_set.remove('Apple')
print(fruit_set)
# Clear set
fruit_set.clear()
print(fruit_set)
# Delete tuple set
del fruit_set
print(fruit_set) # error because it was deleted