'''def first():
    n = 15
    return n


a = first()
print (a)
'''
# Variables in a function are isolated from the rest of the program. 
# When the function ends, they are released from memory and cannot be recovered.

# When mutable data is passed to a function, the function can modify or alter it.
#  These modifications will stay in effect outside the function scope as well. An example of mutable data is a list.

# In the case of immutable data, the function can modify it, but the data will remain unchanged outside the function’s scope. 
# Examples of immutable data are numbers, strings, etc.
# Let’s try to change the value of an integer inside a function:
'''num = 20


def multiply_by_10(n):
    n *= 10
    num = n  # Changing the value inside the function
    print("Value of num inside function:", num)
    print (n)
    return n


multiply_by_10(num)
print("Value of num outside function:", num)  # The original value remains unchanged
'''

# So, it’s confirmed that immutable objects are unaffected by the working of a function. 
# If we really need to update immutable variables through a function,
#  we can simply assign the returning value from the function to the variable.

# Now, we’ll try updating a mutable object through a function:

'''num_list = [10, 20, 30, 40]
print(num_list)


def multiply_by_10(my_list):
    my_list[0] *= 10
    my_list[1] *= 10
    my_list[2] *= 10
    my_list[3] *= 10


multiply_by_10(num_list)
print(num_list)  # The contents of the list have been changed'''


