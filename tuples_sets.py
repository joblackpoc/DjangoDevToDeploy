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