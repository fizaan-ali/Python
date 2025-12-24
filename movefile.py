import os

source = "C:\\Users\\Fizaan\\Desktop\\text.txt" # double \\ for escaping

destination = "C:\\Users\\Fizaan\\Documents\\text.txt" #  destinationlocation # should have to write text.txt at the end

try:
    if os.path.exists(destination):
        print("There is already a file there!")
    else:
        os.replace(source, destination) # we can alos move directories using this!!
        print("'" + source + "'" +  " was moved!")
except FileNotFoundError:
    print("'" + source + "'" + " was not found!")