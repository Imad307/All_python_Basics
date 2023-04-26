'''Duck typing is useful as it simplifies the code and the user can implement the functions without worrying about the data type. 
But this may not be the case all the time. 
The user might not follow the instructions to implement the necessary steps for duck typing. 
To cater to this issue, Python introduced the concept of abstract base classes, or ABC'''
'''
Def:   Abstract Base Classes define a set of methods and properties that a class must implement in order to be considered 
a duck type instance of that class
'''
# Syantax
'''
To define Abstract class we use abc module. The Abstract base class is inherited from the Built-in ABC class.
We have to use the decorator @abstractmethod above the method that we want to declare as an abstract method. 

from abc import ABC, abstractmethod


class ParentClass(ABC):

    @abstractmethod
    def method(self)



Note: Methods with @abstractmethod decorators must be defined in the child class.
     Abstract methods must be defined in child classes for proper implementation of inheritance.

'''
from abc import ABC, abstractmethod


class Shape(ABC):  # Shape is a child class of ABC
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return (self.length * self.length)

    def perimeter(self):
        return (4 * self.length)


square = Square(4)
# this code will not generate an error since abastract methods have been
# defined in the child class, Square