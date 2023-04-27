'''
Aggregation:
     Aggregation follows a HAS-A Approach. In which objects are not bound for life dependency on other object. 
     Instead they only have a reefence to the other class's object. 
     In aggregation, the lifetime of the owned object does not depend on the lifetime of the owner.
'''

class Country:
    def __init__(self, name = None , population = None):
        self.name = name
        self.population = population
    def print_details(self):
        print("Country Name: ", self.name)
        print("population of Country: ", self.population)


class Person:
    def __init__(self, name, country):
        self.name = name
        self.country = country
    def print_details(self):
        print("Person name: ", self.name)
        self.country.print_details()

c = Country("Pakistan", 2500)
p = Person("Imad", c)
p.print_details()

del p
print("")
c.print_details()