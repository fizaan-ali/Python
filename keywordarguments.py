# keyword arguments = arguments preceded by an identifier when we pass them to a function
#                     The order of the argumetns doesn't matter unline positional arguemnts
#                      Python knows the names of the arguments that our functions receive


# now in this these are positional arguments bcz in this position matter
def hello(first, middle, last):
    print("Hello " + first + middle + last)

hello("Fizaan ", "Ali ", "Shafiq")


# now these are keyword arguments -> here we specify our arguments
def hello(first, middle, last):
    print("Hello " + first + middle + last)

hello(last="Shafiq ", first="Fizaan ", middle="Ali ") # here position doesn't matter bcz we specify whihc argument is gonna whihc parameter
