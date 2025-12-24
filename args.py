# *args = parameter that will pack all the arguments into a tuple
#         useful so that a function can accept a varying amount of arguments

# def add(num1, num2):
#     sum = num1 + num2
#     return sum
# print(add(1,2)) # now valid for only two parameters
# print(add(1,2,3)) # now if we increase the parameters from 2 it's going to throw an error
# that's where *args helppp

# def add(*args): # now with '*' operator we are packing our arguments into tuples (args can be named something else no prob)
#     sum = 0
#     for i in args:
#         sum += i
#     return sum

def add(*data): # now with '*' operator we are packing our arguments into tuples (args can be named something else no prob)
    sum = 0
    # to change some data in our arguments, we have to change it to some othre sequence, bcz tuples are immutable
    # data = list(data)
    # data[0] = 0 # now it will change
    for i in data:
        sum += i
    return sum
 
# varying arguments!!!

print(add(1,2)) # 3
print(add(1,2,3,4)) # 10
print(add(1,2,3,4,5,6)) # 21
