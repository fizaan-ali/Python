class Animal:
    def eat(self):
        print("This animal is eating!")

class Rabbit(Animal):
    def eat(self):
        print("This rabbit is eating a carrot")

rabbit = Rabbit()
rabbit.eat() # it will use the method that is inside the rabbit class 