# Inheritence is a way to create a new class from an existing class.
'''
The new class inherits all the non-private fields(variables) and methods of existing class. 
The Existing class is used as a base to create new class.

The 'IS A' Relationship:
    wherever we come accross an IS A Relationship, we can use inheritance.
The Python Object Class:
    Whenever we create a class, by default it is a subclass of Python Object Class. 

    

Synatx And Terminologies;
Terminologies: 
   Parent Class(SuperClass/ Base Class): This class allows to reuse the public properties in another class.
   Child Class(SubClass/ Derived Class): This class is inherits/Extends all the public properties of its SuperClass.
             It has all the public attributes of parent class.
Syntax:

Class ParentClass:
     # Attributes of Parent Class

Class ChildClass(ParentClass):
     # Attributes of childclass 

Example:
'''
'''
class Vehicle:
    def __init__(self, make, color, model):
        self.make = make
        self.color = color
        self.model = model
    def printdet(self):
        print("Manufacturer: ", self.make)
        print("Model: ", self.model)
        print("colour: ", self.color)
class Car(Vehicle):
    def __init__(self, make, color, model, doors):
        Vehicle.__init__(self, make, color, model)
        #super().__init__(make, color, model)# Alternative of above line. 
        self.doors = doors
    def printcardet(self):
        self.printdet()
        print("Doors: ", self.doors)
Check = Car("Suzuki", "Red", "2020", "4")
Check.printcardet()'''

