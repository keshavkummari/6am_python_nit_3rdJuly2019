# Inheritance 

class Animal():
    def __init__(self):
        print("Animal created")

    def whoAmI(self):
        print("I am from Animal Class")

    def eat(self):
        print("Eating")


class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("Dog created")

    def whoAmI(self):
        #Animal.whoAmI(self)
        print("Dog")

    def bark(self):
        print("Woof!")

# Creating an Object and Calling a Class called Dog()
d = Dog()

d.whoAmI()

d.eat()

d.bark()