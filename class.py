class Employee:
    language = "Python" # this is a class attribute
    salary = 120000


harry = Employee()
harry.name = "Harry" # this is an object attriubute / instance attribute
print(harry.name,harry.language, harry.salary)

fizaan = Employee()
fizaan.name = "Fizaan Ali"
print(fizaan.name, fizaan.salary, fizaan.language)

# Here name is object attribute and salary and language are 
# class attributes as they directly belong to the class!    