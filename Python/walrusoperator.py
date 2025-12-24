# walrus operator :=
# new to python 3.8
# assignment expression aka walrus operator
# assigns values to variables as part of a larger expression

# happy = True
# print(happy)
# if you have to directly print and assing in same expreesion you can't 
# print(happy = True)  -> this won't work 
# to do so .,
# print(happy := True) # walrus operator # assigns values to variables as part of largesr expresiion


foods = list()
while True:
    food = input("What food do you like? ")
    if food == "quit":
        break
    foods.append(food)

foods = list()
while (food := input("What food do you like? ")) != "quit":
    foods.append(food)

print(foods)

# != has higher precedence than !=  so put it inside bracketsss
