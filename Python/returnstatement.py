# return statement = function send Python values/objeccts back to the caller
                    #  These values are known as function return values

def multiply(n1, n2):
    result = n1 * n2
    return result

print(multiply(6,8)) # directly print

x = multiply(6,8) # also we can store return values in variables
print(x)