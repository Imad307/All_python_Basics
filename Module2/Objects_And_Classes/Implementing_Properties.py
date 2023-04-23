'''Let's implement the Employee class illustrated below. We’ll start with just adding the properties of the class.'''
'''
# this code will compile
class Employee:
    # defining the properties and assigning them none
    ID = None
    salary = None
    department = None'''
'''
# this code will give a compilation error
class Employee:
    # defining the properties and not assigning them none
    ID
    salary
    department
'''
'''Note that if you do not initialize the values of properties, the Python code will not compile. 
Initializing the values of properties inside the class is necessary.

'''

'''Accessing properties and assigning values#'''
'''To access properties of an object, the dot notation is used:
object.property'''
'''There are two ways to assign values to properties of a class.

1. Assign values when defining the class.
2. Assign values in the main code.

1: Intializing
class Employee:
    # defining the properties and Intializing them with values
    ID = 3789
    salary = 2500
    department = "Human Recources"


# cerating an object of the Employee class
Steve = Employee()



# Printing properties of Steve
print("ID =", Steve.ID)
print("Salary", Steve.salary)
print("Department:", Steve.department)

2: Assigning
class Employee:
    # defining the properties and assigning them None
    ID = None
    salary = None
    department = None


# cerating an object of the Employee class
Steve = Employee()

# assigning values to properties of Steve - an object of the Employee class
Steve.ID = 3789
Steve.salary = 2500
Steve.department = "Human Resources"

# Printing properties of Steve
print("ID =", Steve.ID)
print("Salary", Steve.salary)
print("Department:", Steve.department)
'''
'''
Creating properties outside a class#
Python, being a particularly user-friendly language, provides the user with a feature that most languages usually do not. 
That is, creating properties of an object outside the class. 
Let’s see an example of this by extending the example of the Employee class we discussed above:
Note: The property, title, will only be added to Steve and all other future objects will only have the properties
which are declared in the class.
    
class Employee:
    # defining the properties and assigning them None
    ID = None
    salary = None
    department = None


# cerating an object of the Employee class
Steve = Employee()

# assigning values to properties of Steve - an object of the Employee class
Steve.ID = 3789
Steve.salary = 2500
Steve.department = "Human Resources"
# creating a new attribute for Steve
Steve.title = "Manager"

# Printing properties of Steve
print("ID =", Steve.ID)
print("Salary", Steve.salary)
print("Department:", Steve.department)
print("Title:", Steve.title)
'''

