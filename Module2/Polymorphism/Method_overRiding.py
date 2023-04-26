# Method OverRiding 
'''
This is a process of redefining a parent's class method in a SubClass
In Other Words, if a subclass provides a specific implementation of a method which is already present in one of it's parent 
classes, it is known as Method OverRiding. 

In Method OverRiding:
The Parent's class method is known as OverRidden Method.
The methods in child classes are called OverRidding Methods. 
class Shape:
    def __init__(self):  # initializing sides of all shapes to 0
        self.sides = 0

    def getArea(self):
        pass


class Rectangle(Shape):  # derived form Shape class
    # initializer
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        self.sides = 4

    # method to calculate Area
    def getArea(self):
        return (self.width * self.height)


class Circle(Shape):  # derived form Shape class
    # initializer
    def __init__(self, radius=0):
        self.radius = radius

    # method to calculate Area
    def getArea(self):
        return (self.radius * self.radius * 3.142)


shapes = [Rectangle(6, 10), Circle(7)]
print("Area of rectangle is:", str(shapes[0].getArea()))
print("Area of circle is:", str(shapes[1].getArea()))

'''
'''
Advantages and key features of method overriding#
The derived classes can give their own specific implementations to inherited methods without modifying the parent class methods.

For any method, a child class can use the implementation in the parent class or make its own implementation.

Method overriding needs inheritance, and there should be at least one derived class to implement it.

The methods in the derived classes usually have a dissimilar implementation.'''