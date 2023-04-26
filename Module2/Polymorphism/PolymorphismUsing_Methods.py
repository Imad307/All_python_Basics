# Consider the example of shapes.

class Rectangle:
    def __init__(self, Width = 0, Height =0):
        self.Width = Width
        self.Height = Height
        self.Sides = 4
    
    def getArea(self):
        return (self.Height * self.Width)

class Circle:
    def __init__(self, radius= 0):
        self.radus = radius
        self.Sides = 0
    def getArea(self):
        return (self.radus * self.radus * 3.14)


shapes = [Rectangle(6,10), Circle(7)]

print("Sides of Rectangle: ", str(shapes[0].Sides))
print("Area of Rectangle is: ", str(shapes[0].getArea()))

print("Sides of A Circle: ", str(shapes[1].Sides))
print("Area of a Circle is: ", str((shapes[1]).getArea()))

# We have Implemented the Polymorphism using method class by using a list object which includes all the necessary classes. 
