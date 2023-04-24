'''
There are 5 Types of Inheritances:
1. Single Inheritance
2. Multi-Level Inheritance 
3. Hierarchical Inheritance 
4. Multiple Inheritance
5. Hybrid Inheritance
'''
'''
1. Single Inheritance:
In Sigle Inheritance, There is only a single class extending from another class.
Example:

class vehicle:
    def TopSpeed(self, speed):
        self.topspeed = speed
        print("Top speed is set to: ", self.topspeed)
class car(vehicle):
    def opentrunk(self):
        print("Trunk is Open Now.")

corolla = car()
corolla.TopSpeed(220)
corolla.opentrunk() 
'''

'''
2. Multi-Level Inheritance:
   The type of inheritance in which a class is derived from an other class which is itself derived from another class.
   Example:
   

class Vehicle:  # parent class
    def setTopSpeed(self, speed):  # defining the set
        self.topSpeed = speed
        print("Top speed is set to", self.topSpeed)


class Car(Vehicle):  # child class of Vehicle
    def openTrunk(self):
        print("Trunk is now open of Audi.")


class Hybrid(Car):  # child class of Car
    def turnOnHybrid(self):
        print("Hybrid mode is now switched on.")


priusPrime = Hybrid()  # creating an object of the Hybrid class
priusPrime.setTopSpeed(220)  # accessing methods from the parent class
priusPrime.openTrunk()  # accessing method from the parent class
priusPrime.turnOnHybrid()  # accessing method from the child class
'''

'''
3. Hierarchical Inheritance
The type of inheritance in which more than one class springs out/ extends from a base class.
Example:
A Car is a Vehicle.
A Truck is also a Vehicle.

class Vehicle:  # parent class
    def setTopSpeed(self, speed):  # defining the set
        self.topSpeed = speed
        print("Top speed is set to", self.topSpeed)


class Car(Vehicle):  # child class of Vehicle
    pass


class Truck(Vehicle):  # child class of Vehicle
    pass


corolla = Car()  # creating an object of the Car class
print("Corolla")  # accessing methods from the parent class
corolla.setTopSpeed(220)
volvo = Truck()  # creating an object of the Truck class

volvo.setTopSpeed(180)  # accessing methods from the parent class
'''
'''
4. Multiple Inheritance
The Type of inheritance in which a class is derived from two/more different classes. 
Example: 
Hybrid is an Electric Engine
Hybrid is a combustion engine as well.

class CombustionEngine():  
    def setTankCapacity(self, tankCapacity):
        self.tankCapacity = tankCapacity


class ElectricEngine():  
    def setChargeCapacity(self, chargeCapacity):
        self.chargeCapacity = chargeCapacity

# Child class inherited from CombustionEngine and ElectricEngine
class HybridEngine(CombustionEngine, ElectricEngine):
    def printDetails(self):
        print("Tank Capacity:", self.tankCapacity)
        print("Charge Capacity:", self.chargeCapacity)

car = HybridEngine()
car.setChargeCapacity("250 W")
car.setTankCapacity("20 Litres")
car.printDetails()
'''

'''
5. Hybrid Inheritance: 
   The type of Inheritance which is a combination of both the mutiple and MultiLevel Inheritance. 
Example:
   Combustion Engine is a type of Engine
   Electric Engine is a type of Engine.
   But Hybrid is both an Electric and Combustion Engine.
class Engine:  # Parent class
    def setPower(self, power):
        self.power = power


class CombustionEngine(Engine):  # Child class inherited from Engine
    def setTankCapacity(self, tankCapacity):
        self.tankCapacity = tankCapacity


class ElectricEngine(Engine):  # Child class inherited from Engine
    def setChargeCapacity(self, chargeCapacity):
        self.chargeCapacity = chargeCapacity

# Child class inherited from CombustionEngine and ElectricEngine

class HybridEngine(CombustionEngine, ElectricEngine):
    def printDetails(self):
        print("Power:", self.power)
        print("Tank Capacity:", self.tankCapacity)
        print("Charge Capacity:", self.chargeCapacity)

car = HybridEngine()
car.setPower("2000 CC")
car.setChargeCapacity("250 W")
car.setTankCapacity("20 Litres")
car.printDetails()
'''


