# Prevents a user from creating an object of that class
# + compels a user to override abstract methods in child class

# abstract class -> a class which contains one or more abstract methods
# abstract method -> a method that has a declaration but does not have an implementation

# class Vehicle:

#     def go(self):
#         pass

# class Car(Vehicle):

#     def go(self):
#         print("You drive the car!")

# class Motorcycle(Vehicle):

#     def go(self):
#         print("You drive the motorcycle")

# vehicle = Vehicle()
# car = Car()
# motorcycle = Motorcycle()

# vehicle.go()
# car.go()
# motorcycle.go()


# now to create an abstract class  we have to import 

from abc import ABC, abstractmethod
# abc = abstract base class
class Vehicle(ABC): # now this is abstract class # it only acts as template
    @abstractmethod
    def go(self): # and this is abstract method 
        pass

class Car(Vehicle):
    def go(self):
        print("The car is driving")

class Motorcycle(Vehicle):
    def go(self):
        print("The bike is driving")

# vehicle = Vehicle() # now this won't work this will cause an error bcz we can't create an object of abstract c class
car = Car()
bike = Motorcycle()

car.go()
bike.go()

# by inheriting from abstract class, children classes should have an implementation
# of the abstract methods that are in abstract class, otherwise give error
# le'ts say abstract class has method 'go' now it's child class must have 
# it's definition of 'go' method 