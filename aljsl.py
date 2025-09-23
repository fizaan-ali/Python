with open("log.txt") as file:
    str = file.read()
if("python" in str.lower()):
    print("Word exists!")
else:
    print("Word doesn't exist!")