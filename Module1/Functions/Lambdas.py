# A lambda is an anonymous function that returns some form of data.

# Lambdas are defined using the lambda keyword. Since they return data, it is a good practice to assign them to a variable.

# In the structure above, the parameters are optional.

# Let’s try creating a few simple lambdas.

# Below, we can find a lambda that triples the value of the parameter and returns this new value:

'''triple = lambda num : num * 3  # Assigning the lambda to a variable
num=1
print(triple(num))  # Calling the lambda and giving it a parameter'''

# One more example

'''concat_strings = lambda a, b, c: a[0] + b[0] + c[0]

print(concat_strings("World", "Wide", "Web"))
'''

# A lambda cannot have a multi-line expression. 
# This means that our expression needs to be something that can be written in a single line.

# we can also use conditional statement in lambdas like:
'''
my_func = lambda num:"High" if num<50 else "Low"
print(my_func(60))
'''
