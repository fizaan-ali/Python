# multi-level inheritance -> a derived class (child) inherits another derived (child) class
class Organism: # grandparent
    alive = True

class Animal(Organism): # parent

    def eat(self):
        print("This animal is eating!")

class Dog(Animal): # child 

    def bark(self):
        print("This dog is barking!")


dog = Dog()

print(dog.alive) # inherit from organims class
dog.eat() # inherit from animal class
dog.bark() # it's own attribute
