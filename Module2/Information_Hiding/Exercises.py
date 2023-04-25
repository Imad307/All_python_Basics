'''# Rectangle Area and Perimeter
class Rectangle:
    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def area(self):
         return (self.__length * self.__width)

    def perimeter(self):
        return (2*(self.__length + self.__width))

check = Rectangle(5, 4)
print("rectangle Area: ", check.area())'''

# implement a complete Student Class

class student:
    def __init__(self, name, rollnumber) :
        self.__name = name
        self.__rollnumber = rollnumber
    def getName(self):
        return(self.__name)
    def getRollNumber(self):
        return(self.__rollnumber)
    def setName(self, name2):
        self.__name = name2
    def setRollNumber(self, rollnumber2):
        self.__rollnumber = rollnumber2

steven = student("Imad", "15")
print("Before setting: ", steven.getName(), steven.getRollNumber())
steven.setName("Mohibbi")
steven.setRollNumber("`13")
print("After Setting: ", steven.getName(), steven.getRollNumber())