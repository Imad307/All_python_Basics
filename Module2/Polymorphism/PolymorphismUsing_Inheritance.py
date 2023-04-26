''' We can add new data and methods into derived class using Inheritance. But, What happens when we want to inherit methods or 
properties of from parent class but with different implementation. At that point we use Polymorphism as this falls in Polymorphism
definition(Part of same class but with different Properties)
'''
# Example is Below

class Shape:
    def __init__(self):
        self.Sides = 0
    def getArea(self):
        pass

class Rectangle(Shape):
    def __init__(self, Width = None, Height= None):
        self.Width = Width
        self.Height = Height
        self.Sides = 4
    def getArea(self):
        return(self.Height * self.Width)

class Circle(Shape):
    def __init__(self, Radius):
        self.Radius = Radius
        self.Sides = 0
    def getArea(self):
        return (self.Radius * self.Radius * 3.14)

Shapes = [Rectangle(5,4), Circle(5)]
print("Area of Rectangle: ", str(Shapes[0].getArea()))
print("Area of Circle: ", str(Shapes[1].getArea()))
'''The getArea() method returns the area of the respective shape. 
This is Polymorphism: having specialized implementations of the same methods for each class.'''