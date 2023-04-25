'''
In order to allow controlled access to classes we uses getter and setter methods.

Getters: These methods are used to read the value of property
Setters: These methods are used to modify the property's value.

It is a common convention to use get and set with corresponding members.
i-e, getprperty()  oe setproperty()

Example:
'''
class user:
    def __init__(self, username):
        self.__username = username
    def setusername(self, second):
        self.__username = second
    def getusername(self):
        return(self.__username)

steven = user("steve1")
print("Before Setting: ", steven.getusername())
steven.setusername("steve2")
print("After Setting: ", steven.getusername())