# CLOSURE 
# A closure is a nested function that remembers and uses variables from its outer function
# even after the outer function is finished execution!

def counter():
    count = 0
    def increment():
        nonlocal count
        count += 1
        return count
    
    return increment

f1 = counter()
f2 = counter()
print(f1())
print(f1())
print(f1())
print(f2())
