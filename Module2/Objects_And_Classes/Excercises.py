class Student:
    def __init__(self, name, phy, chem, bio):
        self.name = name
        self.phy = phy
        self.chem = chem
        self.bio = bio

    def totalObtained(self):

        return ( self.phy + self.chem + self.bio)

    def percentage(self):
        Totalmarks = 300
        return ((self.totalObtained()/Totalmarks)*100)

actualoutput = Student('Mark', 80, 70, 90)
print(actualoutput.totalObtained())
print(actualoutput.percentage(), "%")
