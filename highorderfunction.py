# in python, functions are just objects like any other variables or things!
# High order function -> 
# a function that either accepts a function as argument or returns a function

def loud(text):
    return text.upper()

def quiet(text):
    return text.lower()

def hello(func): # high order function -> accepts a function as argument!
    text = func("Hello")
    print(text)

# hello(loud)
# hello(quiet)


def divisor(x):
    def dividend(y):
        return y/x
    return dividend

divide = divisor(2) # divide now points to the same memory locatioin as dividend now if we do divide() it means dividen()


print(divide(10))

# now this is high order function


def outer():
    print("I am outer")
    def inner():
        print("I am inner")
    return inner

f = outer() # f now holds the inner function # it prints I am outer
f() # call the inner function # it prints I am inner