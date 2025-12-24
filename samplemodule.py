# def add(x,y):
#     return x + y

# print(add(2,3))

# so now in the above code while if it is being imported it's going to automatically print 5 bcz imported file starts automatically execute

# the correct method is below

def add(x,y):
    return x + y

if __name__ == '__main__': # if this file is being is being run directly only then execute this block of code
    print(add(2,3)) # now this bock of code will execute only if the file is running directly


# the concept is to put all the declarrations and definitons outside 
# and all executions and protection insdie this 'if __name__ = '__main__' condition
# to avoid iit running during import!!!