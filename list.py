friends = ["Apple", "Orange", 5, 32.12, False, "Carry"] # store values of any datatype
print(friends)
print(friends[1])
print(friends[-1])
friends[1] = "Banana"
print(friends[1])
print(friends) # so unlike strings, lists are mutable
# like we cannot change a character in a string like this str[3] = 'a' (it gives an error)
# but we can change an element in a list like this friends[1] = "Fizaan"
print(friends[1:4]) # slicing works the same way as strins
