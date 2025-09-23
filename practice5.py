# fruits = {
#     "kela": "Banana",
#     "saeb": "Apple",
#     "amrud": "Guava",
#     "aam": "Mango"
# }
# fruit = input("Enter the fruit name in Urdu: ")
 
# print(fruits[fruit]) # or print(fruits.get(fruit))
 

# s = set()

# s1 = int(input("Enter the number 1: "))
# s.add(s1)
# s2 = int(input("Enter the number 2: "))
# s.add(s2)
# s3 = int(input("Enter the number 3: "))
# s.add(s3)
# s4 = int(input("Enter the number 4: "))
# s.add(s4)
# s5 = int(input("Enter the number 5: "))
# s.add(s5)
# s6 = int(input("Enter the number 6: "))
# s.add(s6)
# s7 = int(input("Enter the number 7: "))
# s.add(s7)
# s8 = int(input("Enter the number 8: "))
# s.add(s8)

# print(s)
# print(type(s))

# s = set()

# s.add(18)
# s.add("18")

# print(s)
# print(type(s))

# s = set()
# s.add(1)
# s.add(1.0)
# s.add("1")
# print(s)
# print(len(s)) # why 2? because 1 and 1.0 are considered equal in Python! Despite being of different data types.
# print(type(s))

# d = {}
# name = input("Enter friend's name: ")
# lang = input("Enter programming language: ")
# d.update({name: lang})

# name = input("Enter friend's name: ")
# lang = input("Enter programming language: ")
# d.update({name: lang})

# name = input("Enter friend's name: ")
# lang = input("Enter programming language: ")
# d.update({name: lang})

# name = input("Enter friend's name: ")
# lang = input("Enter programming language: ")
# d.update({name: lang})

# print(d)

s = {8, 7, 12, "Harry", [1,2]}
# we cannot update a list in a set because lists are mutable (changeable) and sets require their elements to be immutable (unchangeable).
# in fact, we cannot add a list to a set at all, as shown in the code above. This will raise a TypeError. 
# print(s) # Gives us an error