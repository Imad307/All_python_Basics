'''
Tuple is similar to list but it contents are immutable but it can contain elements that can be altered like a list. 
They are also ordered. 
'''
car = ("Ford", "Raptor", 2019, "Red")
print(car)

# Length
print(len(car))

# Indexing
print(car[1])

# Slicing
print(car[2:])

# Merge: we can merge two tuple using '+' operator.

# Nested Tuples: we can create a nested tuple by assiging it one or more tuples. 
# Like: merged_tuple = (tuple1, tuple2)

# Search
'''
To check if something is present or not we use 'in' operator 
otherwise we can use index() function to find the exact index of value in the tuple
'''

# Tuples are immutable, so no deletion, addition or appending the tuple. 