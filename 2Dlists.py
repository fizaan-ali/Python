# 2D lists: a list of lists

drinks = ["coffee", "chai", "soda"]
snacks = ["lays", "kurkure", "many more"]
dessert = ["cake", "ice cream", "kulfi"]

food = [drinks, snacks, dessert]

# print(food) # list of lists

print(food[1][2]) # first go the first index of food and then prints the second index value at that list
print(food[2][4]) # index out of range!

# for i in range(3):
#     for j in range(3):
#         print(food[i][j], " " ,end="")
#     print()
