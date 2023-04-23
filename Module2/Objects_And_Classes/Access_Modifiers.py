'''In Python, we can impose access restrictions on different data members and member functions. 
The restrictions are specified through access modifiers. 
Access modifiers are tags we can associate with each member to define which parts of the program can access it directly.
'''
'''
There are two types of modifiers in Python:
Public attributes:
     "Public attributes are those which are available publically withon and without the class."
    Formally, In Python, all methods and properties are publically available. if we have to make a method or property private,
    we have to mention explicitly to python that it is for private purposes. 
    Example:
class Employee:
    def __init__(self, ID, salary):
        # all properties are public
        self.ID = ID
        self.salary = salary

    def displayID(self):
        print("ID:", self.ID)


Steve = Employee(3789, 2500)
Steve.displayID()
print(Steve.salary) 
'''
''' 
Private attributes#
"Private attributes cannot be accessed directly from outside the class but can be accessed from inside the class."

The aim is to keep it hidden from the users and other classes. 
Unlike in many different languages, it is not a widespread practice in Python to keep the data members private 
since we do not want to create hindrances for the users. We can make members private using the double underscore __ prefix.
Exapmles:
'''
'''class Employee:
    def __init__(self, ID, Salary):
        self.__ID = ID  #ID is Private attibute
        self.salary= Salary
steven  = Employee(13, '$1500')
print("Salary is : ", steven.salary)
print('ID is: ', steven.__ID)  # It should Give an Error'''
'''
class Employee:
    def __init__(self, ID, Salary):
        self.ID = ID  
        self.salary= Salary
    def displayID(self):
        print("ID is: ", self.ID)
    def __displaySalary(Self):   #Salary(Instance method for salary)is Private attibute
        print("Salary is: ", Self.salary)
steven  = Employee(13, '$1500')
steven.displayID()
steven.__displaySalary()# This should generate error

'''
'''
Accessing private attributes in the main code#
As discussed above, it is not common to have private variables in Python.

Properties and methods with the __ prefix are usually present to make sure that the user does not carelessly access them. 
Python allows for free hand to the user to avoid any future complications in the code. 
If the user believes it is absolutely necessary to access a private property or a method, 
they can access it using the _<ClassName> prefix for the property or method. 
An example of this is shown below:
'''
class Employee:
    def __init__(self, ID, salary):
        self.ID = ID
        self.__salary = salary # This is a private attribute
steven = Employee(13, 10000)
print("My ID is : ", steven.ID)
print("My Salary is: ", steven._Employee__salary) # Accessing private attribute or property 
# Python does not have protected access modifier unlike other programming languages.

