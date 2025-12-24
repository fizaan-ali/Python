# tuple = collection which is ordered and unchangeable 
#           used to group related data!

student = ("Fizaan Ali", 555, 3.63)

print(student.count(555)) # how many times a certain value is in the list
print(student.count(55)) # it will return 0 bcz 55 is not any element in the list but 555 is!!!

print(student.index(3.63)) # returns the index value of specific value in tuple # if nothing found gives an error


for x in student: # iterate over tuple
    print(x)


if "Fizaan Ali" in student:
    print("Fizaan is here!")

# if "Fizaan" in student: # it's going to return false! bcz the "Fizaan" value is not in tuple but "Fizaan Ali" does both are different!
#     print("Fizaan is here!")
# in returns if something is inside something
