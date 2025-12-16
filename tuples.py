# TUPLES (immutable) --> once created can't be altered
names = ("Fizaan", "Ali", "Shafiq")

print(names[0]) # returns value at specific index

print(names.index("Ali")) # returns the index of the specific value

print(len(names)) # gives length of tuple

print("Ali" in names) # gives true if specific name is in tuple

print(sorted(names)) # creates new sorted tuple doesn't change existing one
print(names)


newTuple = names + ("Ashraf", "ali")

# ("ali") -> this is a string bcz tuples are recognized by commas in python
# ("ali",) -> this is a tuple (single element) bcz there is a comma 

print(newTuple)