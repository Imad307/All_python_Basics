'''
Overloading Operators in Python:
   Operators in python can be overloaaded to operate in a certain user defined way. Whenever operator is used in python its
   corresponding method is invoked to perform its predefined functions. E.g. when '+' is called, __Add__ is invoked in Python.
'''
'''
OverLoading Operators in a User defined Class:
    When a calss is defined it's objects can interract with each other through operators but it is necessary to define behaviour 
    of those operators through operator overlading 

'''

class combine:
    def __init__(self, real, imag) :
        self.real = real
        self.imag = imag
    def __add__(self, other):
        temp = combine(self.real + other.real , self.imag + other.imag)
        return temp
    def __sub__(self, other):
        temp = combine (self.real - other.real , self.imag - other.imag)
        return temp
obj1= combine(3,7)
obj2 = combine(2,5)

obj3 = obj1 + obj2
obj4 = obj1 - obj2

print("After Addition: ", obj3.real, '+ j' , obj3.imag)
print("After subtraction: ", obj4.real, '+ j' , obj4.imag)
'''
You can name the second argument anything, but as per convention, we will be using the word other to reference the other object.
'''