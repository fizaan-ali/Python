# multiple inheritance -> when a child class is derived from more than one parent!

class Prey():
    def flee(self):
        print("This animal flees")

class Predator():
    def hunt(self):
        print("This animal hunts")

class Fish(Prey, Predator): # it inherits from both prey and predator class (multiple inheritance)
    pass

class Rabbit(Prey): # inherits from prey
    pass

class Hawk(Predator): # inherits from predator
    pass

rabbbit = Rabbit()
hawk = Hawk()
fish = Fish()

rabbbit.flee()
hawk.hunt()
fish.flee()
fish.hunt()
