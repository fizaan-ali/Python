with open("this.txt", "r") as file:
    c1 = file.read()
with open("this_copy.txt", "r") as file:
    c2 = file.read()

if(c1 == c2):
    print("Both files are identical!")
else:
    print("Both files are not identical!")