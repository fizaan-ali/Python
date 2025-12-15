marks = {
    "Fizaan": 85, 
    "Ans": 90,
    "Ali": 78,
    "Ahsan": 92,
    0: "Test"
}
print(marks.items()) # print in the form of list of tuples 
print(marks.keys()) # print only keys
print(marks.values()) # print only values

print(marks.update({"Fizaan": 95, "Abdullah": 88})) # update the value of key "Fizaan" and add new key "Abdullah"
print(marks)

print(marks.get("Ans")) # get the values of key "Ans"
print(marks.get("Umer")) # it will return None because the key is not present!
print(marks["Umer"]) # it will give error because the key is not present! 
# key difference between the above two lines!

