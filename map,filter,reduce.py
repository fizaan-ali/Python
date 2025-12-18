# map(), filter(), reduce()
# 1. MAP -> it iterates through a sequence and performs the function on each value of sequence and then returns the updated sequence
numbers = [1,2,3,4]

def double(a):
    return a * 2

# square = lambda a : a ** 2 -> we can also directly use lambda in map function

result = map(double, numbers)
result_ = map(lambda a : a ** 2, numbers)

print(list(result))
print(list(result_))

#2. FILTER -> filter performs the required function on a whole sequence one by one and filter the sequence on behalf of condition in function and returns the updated sequence on basis of true or false

def isEven(n):
    return n % 2 == 0 # this line would return true if it's even otherwise false

result__ = filter(isEven, numbers) # if condition is true the number is in the updated list otherwise not
print(list(result__))

print(list(filter(lambda a: a % 2 != 0, numbers))) # we can also do it one line using lambda function!

# REDUCE -> take a list and reduce it to a single valuee

from functools import reduce # reduce is not avialable directly

expenses = [("Dinner", 80), ("Car", 120)] # list of tuples
# now if you want to calculate the sum of expenses
sum_ = 0
for expense in expenses:
    sum_ += expense[1]

sum = reduce(lambda a, b: a[1] + b[1], expenses)
print(sum)
print(sum_)