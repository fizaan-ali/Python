# CLASSES

class Animal:
    def walk(self):
        print("Walking....")

class Dog(Animal): # inheritance!
    def __init__(self, name, age): #constructor
        self.name = name
        self.age = age
    
    def bark(self):
        print("Woof!")
    

tommy = Dog("Tommy", 8)

print(tommy.name)
print(tommy.age)
tommy.bark()
tommy.walk()

# there's way more things in classes and oop in python as in c++

# MODULES
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def show(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
class Student(Person): # Inheritance
    def __init__(self, name, age, roll_no):
        super().__init__(name, age) # call the parent constructor
        self.roll_no = roll_no
    def show(self):
        super().show()
        print(f"Roll no: {self.roll_no}")

s1 = Student("Fizaan", 17, 555)
s1.show()

