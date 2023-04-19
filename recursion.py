# Recursion is the process in which a function calls itself during its execution. 
#Each recursive call takes the program one scope deeper into the function.
# The recursive calls stop at the base case. 
#The base case is a check used to indicate that there should be no further recursion.

# Let's write a recursive func in which a number is decreasing until it becomes 0

'''def dec_num(n):
    print (n)
    if n ==0: #Base Case
        return
    dec_num(n-1) # A recursive call with different argument

dec_num(5)'''

'''def dec_num(n):
    if n ==0: #Base Case
        return
    dec_num(n-1) # A recursive call with different argument
    print(n)

dec_num(5)'''

# Fibonacci Example 
# We have to find nth number in Fibonacci Series

'''def fib(n):
    if n<=1:
        return 0
    elif n==2:
        return 1
    else:
        return((fib(n-1)+fib(n-2)))
        
print(fib(15))'''

