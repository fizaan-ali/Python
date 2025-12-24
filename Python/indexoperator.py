# INDEX OPERATOR -> gives access to a sequences' elements (str, list, tuples)

name = "fizaan ali"

# if(name[0].islower()):
#     name = name.capitalize()

first_name = name[:6].upper()
last_name = name[7:].lower()

print(first_name)
print(last_name)

# there is also then negative indexing! the last char is -1 and then moving backwards it increases to -2, -3, ......
print(name[-2])