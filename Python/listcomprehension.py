# list comprehension -> a way to create new lists with less syntax
#           can mimic certain lambda functions, easier to read
#           list = [expression for item in iterable]
#           list = [expression for item in iterable if conditional]
#           list = [expression if/else for item in iterable]

# square = []
# for i in range(1,11):
#     square.append(i*i)
# print(square)

# [expression for item in iterable]

squares = [i*i for i in range(1,11)]
print(squares)

# students = [100,90,80,70,60,50,40,30,20,10]
# passed_students = list(filter(lambda x : x >= 60, students))
# print(passed_students)

# [expression for item in iterable if conditional]

students = [100,90,80,70,60,50,40,30,20,10]

passed_students = [i for i in students if i >= 60]

print(passed_students)

# [expression (if/else) for item in iterable]

students = [100,90,80,70,60,50,40,30,20,10]

passed_students = [i if i>=60 else "Failed" for i in students]

print(passed_students)