# sort() method -> specifically used with lists
# sorted() function -> used with iterables (strings, tuple, lists)

students = ["Fizaan", "Ans", "Suleman", "Fahad", "Masood", "Ali"]
students_ = students
students.sort() # it returns nothing it just sorts the original list!
# sort can take two optional keyword arguments, key and reverse
students_.sort(reverse=True) # do in reverse order!

print(sorted(students)) # sorted() it returns the sorted iterable it doesn't change the orginal iterable
#sorted() -> one mandatory argument (an iterable) and two optional key and reverse
print(students)
print(students_)

# index:      0     1    2 
std =  [("Fizaan", "A", 55),
        ("Ans", "B", 64),
        ("Fahad", "C", 77),
        ("Suleman", "D", 51)
        ]

# std.sort() # it sorts them on base of first column

grade = lambda grades:grades[1]
std.sort(key=grade) # grade -> function object will give us the 2nd column

print(std)


std.sort(key=lambda x : x[2], reverse=True) # now it will reverse sort based on basis of index 2 (roll no)
print(std)





data = (("Fizaan", 3.63),
        ("Ali", 3.2),
        ("Ans", 2.8),
        ("Suleman", 3.4))

sorted_data = sorted(data) # it sorts and returns sorted tuple based on first index means alphabetically 
print(sorted_data)

sorted_data_ = sorted(data, key=lambda x : x[1]) # now it sorts based on second index (cgpa)
print(sorted_data_)
sorted_data__ = sorted(data, key=lambda x: x[1], reverse=True)
print(sorted_data__) # now it should be 'Fizaan' on top of list based on cgpa 😎
