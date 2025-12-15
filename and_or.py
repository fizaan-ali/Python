# 'or' and 'and' does not always return true or false ==> they return one of the actual operand 
# falsy values -> treated as false (any null value) e.g [],{},(),False,0, Null etc
# truthy values -> treated as true any non-null value 

# AND -> returns the first falsy value and if not returns last value 
print(5 and 10)
print(True and "Fizaan")
print([] and True)
print(False and 0)
print(0 and 10)

# OR -> returns the first truthy value and if not returns last value

print(5 or 10)
print(False or "Fizaan")
print(0 or [])
print(2 or False)
print(False or 2)