'''
super() function comes into play when we use inheritence. It allows us to use attributes in childclass without naming parent class
Note: Make sure to add parentthesis at the end otherwise it will a compilation error.'''
'''
Use cases of the super() function#

1. Accessing parent class properties#
Consider the fields named fuelCap defined inside a Vehicle class to keep track of the fuel capacity of a vehicle. 
Another class named Car extends from this Vehicle class. 
We declare a class property inside the Car class with the same name, i.e., fuelCap, but with a different value. 
Now, if we want to refer to the fuelCap field of the parent class inside the child class, we will have to use the super() function.


class Vehicle:  # defining the parent class
    fuelCap = 90


class Car(Vehicle):  # defining the child class
    fuelCap = 50

    def display(self):
        # accessing fuelCap from the Vehicle class using super()
        print("Fuel cap from the Vehicle Class:", super().fuelCap)

        # accessing fuelCap from the Car class using self
        print("Fuel cap from the Car Class:", self.fuelCap)


obj1 = Car()  # creating a car object
obj1.display()  # calling the Car class method display()


2. Calling the parent class methods#
Just like properties, super() is also used with methods. 
Whenever a parent class and the immediate child class have any methods with the same name, 
we use super() to access the methods from the parent class inside the child class. Let’s go through an example:

class Vehicle:  # defining the parent class
    def display(self):  # defining display method in the parent class
        print("I am from the Vehicle Class")


class Car(Vehicle):  # defining the child class
    # defining display method in the child class
    def display(self):
        super().display()
        print("I am from the Car Class")


obj1 = Car()  # creating a car object
obj1.display()  # calling the Car class method display()


3. Using with initializers#

Another essential use of the function super() is to 
call the initializer of the parent class from inside the initializer of the child class.
Note: It is not necessary that the call to super() in a method or an initializer is made in the first line of the method.
class ParentClass():
    def __init__(self, a, b):
        self.a = a
        self.b = b


class ChildClass(ParentClass):
    def __init__(self, a, b, c):
        self.c = c
        super().__init__(a, b)


obj = ChildClass(1, 2, 3)
print(obj.a)
print(obj.b)
print(obj.c)

Example 2:
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
Check.printcardet()

'''