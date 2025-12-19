# ANNOTATIONS
"""In python, we generally don't specify the datatypes of arguments and return 
values. But we can also specify using annotations"""

def inc(n): # without any annotations can accept any value
    return n + 1

# we can also specify 

def inc_(n : int) -> int: # first int tells that only accept integers, second int tells that the return type is int
    return n + 1

print(inc_(2.8))

count : int = 0
print(type(count))

# but these are not forced python will do what it suits at runtime!!!
# python is going to ignore these annotations