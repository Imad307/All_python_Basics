# Composition is a relationship in which other class objects are accessed by a classS
'''
Composition Class is a PART-OF relationship. So, There is a class object which owns other class objects for lifetime. 
That means they are dependent on owner class object as long as owner lifetime.
Note: Lifetime of owned object depends on owner's lifetime. 
'''
# Example is a Car, which has doors, tires, colour and a engine
 
class Engine:
    def __init__(self, capacity):
        self.capacity = capacity
    def printdetails(self):
        print("Engine Capacity: ", self.capacity)
class tires:
    def __init__(self, tire=0) -> None:
        self.tire = tire
    def printdetails(self):
        print("Number of tires: ", self.tire)
class doors:
    def __init__(self, door):
        self.door = door
    def printdetails(self):
        print("Number of doors: ", self.door)

class car:
    def __init__(self, eng, tr,dr,color):
        self.engobj = Engine(eng)    # Creating objects withon class 
        self.tireobj = tires(tr)
        self.doorobj = doors(dr)
        self.colour = color
    def printdetails(self):
        self.engobj.printdetails()
        self.tireobj.printdetails()
        self.doorobj.printdetails()
        print("Car Colour is: ", self.colour)
Car = car(3000, 4, 2, "Black")
Car.printdetails()
