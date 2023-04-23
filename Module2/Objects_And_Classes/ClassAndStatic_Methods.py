'''
As discussed in instance methods, there are three methods 
1. Instance 
2. Class
3. Static

Class Methods:
  "Class methods are accessed using the class name and can be acessed without creating a class object."
  Class methods work with class variables and are accessible using the class name rather than its object. 
  Since all class objects share the class variables, class methods are used to access and modify class variables.
  -> Syntax:
     To declare a method as a class method, we use the decorator @classmethod. 
     cls is used to refer to the class just like self is used to refer to the object of the class. 
     You can use any other name instead of cls, but cls is used as per convention, and we will continue to use this convention.
  Note: Just like instance methods, all class methods have at least one argument, cls.

  class MyClass:
    classVariable = 'educative'

    @classmethod
    def demo(cls):
        return cls.classVariable
'''
'''class player:
    teamname = 'Pakistan'
    def __init__(self, name):
        self.name = name
    @classmethod
    def getTeamName(cls):
        return cls.teamname

print(player.getTeamName())'''
'''Note: I made mistake of putting cls.getTeamName instead of cls.teamname'''
'''class Player:
    teamName = 'Pakistan'  # class variables

    def __init__(self, name):
        self.name = name  # creating instance variables

    @classmethod
    def getTeamName(cls):
        return cls.teamName


print(Player.getTeamName())'''


'''Static methods#
Static methods are methods that are usually limited to class only and not their objects. 
They have no direct relation to class variables or instance variables. 
They are used as utility functions inside the class or when we do not want the inherited classes to modify a method definition.
Note: Static methods can be accessed using the class name or the object name.

Syntax:
class MyClass:

    @staticmethod
    def demo()
        print("I am a static method")
'''
'''class player:
    teamname = 'Pakistan'  # Class Variable 
    def __init__(self, name, salary):
        self.name = name   # Instance Variable 
        self.salary = salary
    def tax(self):         #Instance Method
        return (self.salary*0.15)
    @classmethod    # Class Method 
    def Fetchteam(cls):
        return cls.teamname
    @staticmethod   # Static Method 
    def dice():
        print("This is a static print method")
p1 = player('Do it', 100000)
print(p1.name)
# Static Method can be called by object or class 
p1.dice()
player.dice()
# Class method can only be called by class 
print(player.Fetchteam())
# Instance methods can be used by objects 
print("Tax on a salary: ", p1.tax())
'''
'''Static methods do not know anything about the state of the class, i.e., they cannot modify class attributes. 
The purpose of a static method is to use its parameters and produce a useful result.

Suppose that there is a class, BodyInfo, containing information about the physical attributes of a person. 
We can make a static method for calculating the BMI of any given weight and height:'''

'''class BodyInfo:

    @staticmethod
    def bmi(weight, height):
        return weight / (height**2)


weight = 75
height = 1.8
print(BodyInfo.bmi(weight, height))'''