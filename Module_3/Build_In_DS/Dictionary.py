'''
Dictionary is not like lists or tuples. It has somewhat complex structure.
In real world, A dictionary book has some keys to find a value. In simple words, it store information in words and meanings.
Python, Follows the same structure. 
'''
# A Distionary stores key-value pairs where each unique key is an index which holds it's value associated with it
# Key: Value, also distionary contents are stored in curly braces {}
# Example is below:
'''my_dict ={}
print(my_dict)
my_dict = {"imad": 11, "faizan":22, "Mukarrum":33, "Afash" : 44}
print(my_dict)'''
# Note: Dictionary is an unordered data structure so mostly it will not give the output in the form data is given to it.

# The dict() contructor:

new_dict = dict(Batman= 123, Imad = 1234, Faizan = 234, Mukarrum = 789)
print(new_dict)
# Alternative Approach
'''new_dict = dict([('batman',123), ('Imad', 345), ('faizan', 789)])
print(new_dict)'''
# Accessing The Values:
'''
This is where we can get an advantage over lists and tuples. Because in lists and tuples we have to keep track of indeces due to 
linearity but dictionary is an unordered data structure. Here, we can access the value by enclosing it's key in sqaure brackets[].
Alternatively, we can also use
 a_dictionary.get(key)
'''

'''print(new_dict['Batman'])
print(new_dict.get('Faizan'))
'''
# Adding/Updating Entries into Distionaries
'''new_dict["Ala"] = 4345 # Adding new entry
print(new_dict)'''
new_dict["Ala"] = 23467 # Updating the entry
print(new_dict)
# Deeleting Entry
'''
We can use 'del' to delete an entry in dictionary. Also we can use pop() or popitem() for deleting and using the deleted item.
'''
# del method
'''del new_dict["Ala"]
print(new_dict)'''
#pop method
Imad = new_dict.pop("Imad")
print(Imad)
print(new_dict)
# popitem() method: This removes the latest added item and return it as a tuple (key, value)
Ala = new_dict.popitem()
print(new_dict)
print(Ala)
print(len(new_dict))
#Checking Existence in Dictionary using 'in' or 'not in' operator
print("Batman" not in new_dict)

# Copying Contents of dictionary: we can copy dictionary contents using update() method in python
old_dict = dict(cheema = 90, sheeds = 100)
new_dict.update(old_dict)
print(new_dict)
i = 6
ai = 7
index = 0
new_dict[i] = 5
print(new_dict)
if ai not in new_dict:
    new_dict[ai] =  index
print(new_dict)
