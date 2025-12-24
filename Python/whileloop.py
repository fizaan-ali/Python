# while loop = a statement that will execute it's block of code until the condition remains true

name = ""

while len(name)==0:
    name = input("Enter your name: ")

print("Hello " + name)


# the following code is going to do the same job!
name_ = None

while not name_:
    name_ = input("Enter your name: ")

print("Hello " + name_)