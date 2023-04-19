# In Python, one function can become an argument for another function. This is useful in many cases.

# ->Let’s make a calculator function that requires the add, subtract, multiply, or divide function 
#  along with two numbers as arguments.

# Using Simple Functions:

'''def add(n1,n2):
    return n1+n2
def subtract(n1,n2):
    return n1-n2
def multiply(n1,n2):
    return n1*n2
def divide(n1,n2):
    return n1/n2

def calculator (operations, n1, n2):
    return operations(n1,n2)

res= calculator(multiply, 5, 31)
print(res)'''

# Using Lambdas 

'''def calculator(operations, n1, n2):
    return operations(n1,n2)
n1= 50
n2 = 10
print(calculator (lambda n1,n2: n1 * n2 , n1, n2))
'''

# The built-in map() function creates a map object using an existing list and a function as its parameters. 
# This object can be converted to a list using the list() function.

# The template for map() is as follows:
 #  map(function, list)
# The function will be applied, or mapped, to all the elements of the list.


# Below, we’ll use map() to double the values of an existing list:
'''num_list = [1,5,10,25]
double_list= map(lambda a: a*2, num_list)
print(list(double_list))
print(num_list)
'''
# This creates a new list. The original list remains unchanged.

# filter() filters elements from a list if the elements satisfy the condition that is specified in the argument function.
'''numList = [30, 2, -15, 17, 9, 100]

greater_than_1 = list(filter(lambda n: n > 1, numList))
print(greater_than_1)'''
# just like map(), filter() returns a new object without changing the original list.








