'''
Duck Typing is the most useful concept in OOP in Python. 
Using Duck Typing, we can implement Polymorphism without using Inheritance
'''
# we say that if an object swims like a duck,quacks like a duck,eats like a duck or in short acts like a duck,that object is a duck
'''
Dynamic Typing: 
    Dynamic typing allows us to change the type of object later in code. 
    Due to dynamic nature of python, duck typing allows user to use any object that provides the required behaviour without 
    the contraint that it has to be a subclass.
'''
# Implementing Duck Typing 

class Dog:
    def speak(self):
        print("Woof Woof")
class Cat:
    def speak(self):
        print("Meow Meow")
class AnimalSound:
    def Sound(self, animal):
        animal.speak()

sound = AnimalSound()
dog = Dog()
cat = Cat()

sound.Sound(cat)
sound.Sound(dog)
# Conclucion 
'''
Now coming back to why it is called Duck typing: So, if a bird speaks like a duck, swims like a duck, 
and eats like a duck, that bird is a duck.
Similarly, in the above example, the animal object does not matter in the definition of the Sound method as long as 
it has the associated behavior, Speak(), defined in the object’s class definition. 
In layman terms, since both the animals, dog and cats, can speak like animals, they both are animals. 
This is how we have achieved polymorphism without inheritance.
'''