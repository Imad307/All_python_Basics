# Make a function for a Factorial 

def factorial(n):
    if n==1 or n==0:
        return 1
    elif n<0:
        return "False Input"
    else:
        return n*factorial(n-1)

print(factorial(10))