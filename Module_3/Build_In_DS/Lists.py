'''
Lists can contain multiple datatypes and store data in a linear form through indexing just like strings(have only one datatype)
'''
'''Imad_Adrees = ["Mohibbi", "David", 500]

print(Imad_Adrees) # Will print whole list 

# It will print first index 

print(Imad_Adrees[0])
# Print last index
print (Imad_Adrees[-1])
# Also list are mutable 

Imad_Adrees[-1] += 500
print(Imad_Adrees[-1])
'''
'''# Using Range(): range() can also be converted into list using list() casting. e.g.
seq = range(0,10)
num_list = list(seq)
print(num_list)'''

'''# With some more addition to this concept
seq_1 = range(3, 46, 3)  # Generating multiples of 3 but it does not include last end value so 46 is written instead of 45
mul_3 = list(seq_1)    # Converting range into list using list() casting  
print(mul_3)   # It prints the list of multiples of 3'''

# List-Ception

'''my_list = [["Imad", 23], ["Afsah", 25], ["faizan", 20], ["Mukarram", 13]]
#print(my_list[0])
my_list.append(["Nasreen", 47])
print(my_list)'''
'''The nested lists do not even need to be of the same size! This is not something we can find in many other languages.'''

# Sequential Indexing: To access the elements of a list or a string which exists inside another list, 
# we can use the concept of sequential indexing.
'''print (my_list[1]) # Accessing 2nd member of my_list
print(my_list[1][0]) # Accessing 1st member of 1st member of my_list-i-e "Afsah"
print(my_list[1][0][0])  # Accessing 1st letter of 1st member of 2nd member of my_list -i-e A  '''

# Merging two lists 
'''
One way is to use '+' operator between two lists 
Second way is to use extend() property of lists 
'''
list_1 = [0,1,2,3,4,5,6]
list_2 = [7,8,9,10]
list_3 = [11,12.13,14,15]

# print(list_1 + list_2 + list_3)
list_1.extend(list_2)
list_1.extend(list_3)
print(list_1)
