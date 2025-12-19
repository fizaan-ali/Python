class Student:
    # the dog class
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __gt__(self, other):
        return True if self.age > other.age else False
    def __add__(self, other):
        return self.age + other.age
    def __str__(self):
        print("Name: " + self.name)
        print("Age: ", self.age)
        return ""
    
ans = Student("Ans", 22)
fizaan = Student("Fizaan", 17)

print(fizaan > ans) # now fizaan > ans calls fizaan.__gt__(ans)
print(fizaan + ans) # adds age of both fizaan and ans
print(fizaan)


# | Operator | Dunder method |
# | -------- | ------------- |
# | `>`      | `__gt__`      |
# | `<`      | `__lt__`      |
# | `==`     | `__eq__`      |
# | `!=`     | `__ne__`      |
# | `>=`     | `__ge__`      |
# | `<=`     | `__le__`      |


# | Operator | Dunder         |
# | -------- | -------------- |
# | `+`      | `__add__`      |
# | `-`      | `__sub__`      |
# | `*`      | `__mul__`      |
# | `/`      | `__truediv__`  |
# | `//`     | `__floordiv__` |
# | `%`      | `__mod__`      |



