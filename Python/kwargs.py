# **kwargs = parameter that will pack all the arguments into a dictionary
#           useful so that a function can accept a varying amount of 
#           'keyword arguments'

# def hello(first, last):
#     print("Hello " + first + last)
# hello(first="Fizaan", middle="Ali", last="Shafiq") # now let's say if i have more keyword arguments so then it's going to throw an erro

# to solve this we use **kwargs
def hello(**kwargs):
    # print("Hello " + kwargs['first'] + kwargs['middle'] + kwargs['last'])
    print("Hello,", end=" ")
    for key, value in kwargs.items():
        print(value, end=" ")
    print() # for nl

# in this way we can add multiple keyword arguments
hello(first="Fizaan", middle="Ali", last="Shafiq") 
hello(title="Hafiz", first="Ans", middle="Ali", last="Bhatti")
hello(first="Abdullah")

# it is not mandatory to write **kwargs we can write anythin like **kw but 2 asterisks ** are necessary!