'''In Python there are two type of properties:
Class Variables:
The Class Variables are shared by all instances or objects of class. A change in class variable will change the value of that 
proprty in all  objects of that class
Instance Variables:
The Instance variables are unique to each instance or object. A change in the instance variable will only affect the property of 
that object only.'''

'''->"Class variables are defined outside the initializer and instance variables are defined inside the initializer."'''

'''Example:
'''
'''class myclass:
    team = "Pakistan"
    teammembers = []
    def __init__(self, name):
        self.name = name
        self.formerteams =[]
        self.teammembers.append(self.name)


p1 = myclass("imad")
p1.formerteams.append("UAE")
p2 = myclass("Faizan")
p2.formerteams.append("Iran")

print("Name1:" , p1.name)
print("team: ", p1.team)
print("Teammembers: ", p1.teammembers)
print("Name2: ", p2.name)
print("team: ", p2.team)
print("Teammembers: ", p2.teammembers)

'''
