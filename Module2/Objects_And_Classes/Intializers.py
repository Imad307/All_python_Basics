'''Intializers is used to intialize the objects of a class. It’s used to define and assign values to instance variables.
The initialization method is similar to other methods but has a pre-defined name, __init__.

The double underscores mean this is a special method that the Python interpreter will treat as a special case.

The initializer is a special method because it does not have a return type. 
The first parameter of __init__ is self, which is a way to refer to the object being initialized.
Example:
class Employee:
    # defining the properties and assigning them None
    def __init__(self, ID, salary, department):
        self.ID = ID
        self.salary = salary
        self.department = department


# creating an object of the Employee class with default parameters
Steve = Employee(3789, 2500, "Human Resources")
Steve.title ="Manager"
# Printing properties of Steve
print("ID :", Steve.ID)
print("Salary :", Steve.salary)
print("Department :", Steve.department)
print("Title : ", Steve.title)
'''
'''
My Example:
''''''
class Imad:
    #Creating the properties and assigning them None
    def __init__(self, id, Namei, dish):
        self.id = id
        self.Namei= Namei
        self.dish= dish
#Creating an object of Imad with default parameters
Ima = Imad(1, "iman", "Biryani")
Ima.drink = "Badam Dhodh"
print("ID : ",Ima.id )
print("Namei : ", Ima.Namei)
print("dish: ", Ima.dish )
print("Drink: ", Ima.drink)'''

'''Initializer with optional parameters#'''
'''class Employee:
    # defining the properties and assigning None to them
    def __init__(self, ID=None, salary=0, department=None):
        self.ID = ID
        self.salary = salary
        self.department = department


# creating an object of the Employee class with default parameters
Steve = Employee()
Mark = Employee("3789", 2500, "Human Resources")

# Printing properties of Steve and Mark
print("Steve")
print("ID :", Steve.ID)
print("Salary :", Steve.salary)
print("Department :", Steve.department)
print("Mark")
print("ID :", Mark.ID)
print("Salary :", Mark.salary)
print("Department :", Mark.department)

'''