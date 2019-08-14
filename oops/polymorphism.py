"""
Polymorphism is based on the greek words Poly(Many) and Morphism(Forms).

We will create a structure that can take or use of many forms of objects.

"""
class Animal:
    def __init__(self, name=''):
        self.name = name
    def talk(self):
        #pass  # Empty
        print(self.name,"Welcome to Animal World")

class Cat(Animal):
    def talk(self):
        print(self.name,"Meow!")
 
class Dog(Animal):
    def talk(self):
        print(self.name, "Woof!")


a = Animal('Lion')
a.talk()

b = Cat('Missy')
b.talk()

c = Dog('Rocky')
c.talk()