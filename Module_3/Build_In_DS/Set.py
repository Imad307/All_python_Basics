# A set is a collection of unorderderd data items.
'''
Data is not indexed so we cannot access data using indeces or get(). It is a simplest data structure in python. 
Mutable data structures like lists and dictionaries cannot be added to sets. However, we can add tuples in it.
Set can contain Numbers, Strings, Boolean, Tuples. These are enclosed in curly brackets{} 
'''
#Creating A Set
#ran = {"Educative", 55, 115.15, (True, False)}
#print(ran)
#print(len(ran))

# The Set() Constructor
'''
The set() constructor is an alternative way to create a set. It gives us the advantage of creaing an empty set.
'''
empt = set()
print(empt)
ran = set({"Educative", 55, 115.14, (True, False)})
print(ran)

# Adding Elements into sets 
''' To add a single element into a set we use add() method and to add multiple elements to a set we use update()
But, Inputs to update can only  be lists, tuples, strings or sets '''
   # Adding a single element
ran.add(35)
print(ran)
  # Adding multiple items 
ran.update(("Imad", 45))
print(ran)
ran.discard("Imad") # Does not give an error if element is not found.
print(ran)
#ran.remove(1)  it gives an error if element not found

# Iterating a Set
'''The For loop can be used to iterate an unordered data strtucture like sets. but we will not know in which order iterator
moves meaning elements will be picked randomly.'''
even_list = [2,4]
set_5 = {6,7,8,9,10,11,12,13,14,15,94}
print(set_5)
for num in set_5:
    if(num %2 ==0):
        even_list.append(num)
print(even_list)