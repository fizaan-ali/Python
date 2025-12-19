# FILE HANDLING

file = open("file_.txt", "w")

content = "This is Fizaan Ali writing the file handling code!"

file.write(content)

file.close()

# but with with it automatically going to close the file at the end so we don't have to explicitly write

with open("file_.txt", "r") as file:
    content = file.read()
    print(content)

