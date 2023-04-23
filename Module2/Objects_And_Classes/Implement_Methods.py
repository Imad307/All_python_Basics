'''There are 3 types of methods:
1. Instance Methods (we will commonly call it methods)
2. Static Methods
3. Class Methods

Note: we will use 'methods' for 'instance methods' and for static & classs methods we will use their specific names. This convention
is due to fact that instance methods are used extensively.

-> Instance Metods(Methods):
      "    A method is a group of statements that perform some operations that may or may not retirn a result."
    Method Parameters: Method parameters make it possible to pass values to method. In Python, the first parameter of the method
    should always be 'self' and then followed by remaining parameters. 
    Return statement:
    "There is no need to specify the return type since data types are not specified in Python."
    The self argument:
    One of the major differences between functions and methods in Python is the first argument in the method definition. 
    Conventionally, this is named self. The user can use different names as well, 
    but self is used by almost all the developers working in Python. 
    We will also be using this convention for ease of understanding.

This pseudo-variable provides a reference to the calling object, that is the object to which the method or property belongs to.
If the user does not mention the self as the first argument, the first parameter will be treated for reference to the object.
Note: The self argument only needs to be passed in the method definition and not when the method is called.'''

'''class employee:
    def __init__(self, ID=None, salary= None, Department=None) :
        self.ID = ID
        self.salary = salary
        self.Department = Department
    def tax(self):
        return(self.salary*0.54)
    def salrypday(self):
        return((self.salary - (self.tax()))/30)
    
Steve = employee(13, 100000, "TCE")

print("Name: Steve and ID: ", Steve.ID)
print("Total Salary: ", Steve.salary)
print("Taxes on steve salary: ", Steve.tax())
print("Perday salary after taxes: ", Steve.salrypday())
'''

'''
Method overloading:
"Overloading refers to making a method perform different operations based on the nature of its arguments."

Unlike in other programming languages, methods cannot be explicitly overloaded in python but implicitly overloaded.
In order to include optional parameters, we assign default values to those arguments rather than creating a duplicate method
with the same name. if users chooses not to assign a value to optional parameter a default value is assigned to the variable. 
'''
'''Method Overloading Example:
class classA:
    
    def __init__(self, marks = None, Name = None, ID = None ):
        self.Name = Name
        self.ID = ID
        self.marks = marks
        
    def classb(self, a,b,c=0,d=None):
        print("a: ", a)
        print("b: ", b)
        print("c: ", c)
        print("d: ", d)

steve = classA()

print("ClassB1")
steve.classb(1,2)
print("\n")
print("ClassB2")
steve.classb(1,2,3,4)
print("\n")
print("ClassB3")
steve.classb(1,2,3)
print("\n")
'''
'''
Advantages of method overloading#
One might wonder that we could simply create new methods to perform different jobs rather than overloading the same method. 
However, under the hood, overloading saves us memory in the system. 
Creating new methods is costlier compared to overloading a single one.

Since they are memory-efficient, overloaded methods are compiled faster compared to different methods, 
especially if the list of methods is long.
An obvious benefit is that the code becomes simple and clean. We don’t have to keep track of different methods.

Polymorphism is a very important concept in object-oriented programming. Method overloading plays a vital role in its implementation.
'''