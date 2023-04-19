# The while loop keeps iterating over a certain set of operations as long as a certain condition holds True.
n=249
a=n
print(n%10)
while a>=10:
    a//=10
print(a)


# Iteration vs. Recursion
# If we observe closely, there are several similarities between iteration and recursion. 
# In recursion, a function performs the same set of operations repeatedly but with different arguments.
# A loop does the same thing except that the value of the iterator and 
# other variables in the loop’s body change in each iteration.
# Figuring out which approach to use is an intuitive process. 
# Many problems can be solved through both.
# Recursion is useful when we need to divide data into different chunks. 
# Iteration is useful for traversing data and also when we don’t want the program’s scope to change.