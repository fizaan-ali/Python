class Animal:
    alive = True

    def eat(self):
        print("This animal is eating!")

    def sleep(self):
        print("This animal is sleeping")
 
class Rabbit(Animal): # Rabbit class is child of Animal class -> it's going to inherit from Animal class
    def run(self):
        print("This rabbit is running!")

class Fish(Animal): # also child class can have it's own attributes as well
    def swim(self):
        print("This fish is swimming")

class Hawk(Animal):
    def fly(self):
        print("This hawk is flying")


rabbit = Rabbit()
fish = Fish()
hawk = Hawk()

print(rabbit.alive)
rabbit.eat()
fish.sleep()    
rabbit.run()
fish.swim()