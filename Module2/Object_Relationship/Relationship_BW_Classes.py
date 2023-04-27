'''
While Inheritance represents a relationship betweeen classes, there are situations where there are relationships between objects.
Now we have to use different class objects to create the design of an Application. 
This means that independent class objects has to find a way to interact with each other. 
'''
'''
There are three types of Relationships 
1. IS A 
2. Part-of
3. Has-a 
'''
# My Memory says: Inheritance is (IS A) Relationship.
'''
Part-Of:
   In this realtionship, one class object is a component of another class object. 
   Given Two Classes: Class A and Class B they are in a Part-of relation if a Class A Object is a part of Class B Object or Vice versa
   Any Instance of component class can only be created inside the main class. 
   Eample: Class B and Class C has different implementations but can only be created once Object for A class is created. 
   Hence, Part-of is Dependent relationship.
   '''
'''
Has-a: 
    This is a slightly concrete relationship. A relationship is Has-a Relationship if one or both needs other's object to perform 
    an operation but both classes can exist independently. 
    This represents that a class Has-a refernece to an object of other class but does not decide the lifetime of other class's
    refenced object.
'''
# Note: Python uses top down approch, so make sure to define class prior to creating object for the class. 
'''
Association#
In object-oriented programming, association is the common term for both the has-a and part-of relationships 
but is not limited to these. Two objects are in an association relationship is a generic statement, 
which means that we don’t worry about the lifetime dependency between the objects.
'''