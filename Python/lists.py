# list = store multiple items within a single variable


food = ["pizza", "paratha", "chai", "anda"]
# you can always update the list after the list is being created!

food[3] = "biryani"

# print(food[4]) # out of range error

# print(food[3])


# LIST FUNCTIONS:
food.append("coffee") # adds at the end
food.remove("pizza") # removes specific value
food.pop(1) # removes the value at that index -> if index is not given it's going to remove the last value
food.insert(0, "cake") # adds value at specific index
food.sort() # sorts out the list
food.clear() # deletes all elements in a list

for item in food: # we can easily iterate over the list using for loop!
    print(item)