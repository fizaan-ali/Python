# with open('test.txt') as file:
#     print(file.read())
# # automatically closes the file

# print(file.closed) # checks if file is closed or not!

try:
    with open('test.txt') as file:
        print(file.read())
except FileNotFoundError:
    print("That file was not found!")

