# POLYMORPHISM
class Dog:
    def eat(self):
        print("Eating dog food!")
    
class Cat:
    def eat(self):
        print("Eating cat food!")

animal1 = Dog()
animal2 = Cat()

animal1.eat() # it will call eat for dog
animal2.eat() # it will call eat for cat