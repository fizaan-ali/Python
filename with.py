file = open("file.txt")
print(file.read())
file.close()

# The same code can be written with the 'with' statement.

with open("file.txt") as file:
    print(file.read())

# It automatically closes the file when you're out of 'with' indentation!
# No need to explicitly closing the file.