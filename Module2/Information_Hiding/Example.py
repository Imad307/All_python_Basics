# A login for users

class user:
    def __init__(self, username, password):
        self.__username = username
        self.__password = password
    def login(self, username, password):
        if((self.__username.lower()==username.lower()) and (self.__password.lower()==password.lower()) ):
            print("Access granted")
        
        else:
            print("Invalid Credentials")

steven = user("steve", "Anc123")
steven.login("steve", "Anc123")
steven.login("steve", "abc123")
'''
Note: For encapsulating a class,
All the properties should be private and any access to the properties should be through methods such as getters and setters.
'''