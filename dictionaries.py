student = { "name" : "fizaan", "age" : 8}

print(student["name"]); print(student["age"])
student["subject"] = "IT"
student["age"] = 17

print(student["name"]); print(student["age"])

print(student.get("semester", 3)) 
# get returns the specific value of the key if not found returns none 
# there is also an option for putting default value if not found returns defualt value as 3 in above
del student["subject"]
print(student.keys())
print(student.values())
print(student.items())

studentcopy = student.copy()
print(studentcopy)

