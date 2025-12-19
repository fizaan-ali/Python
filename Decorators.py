# DECORATORS
def logtime(func):
    def wrapper():
        # do something before 
        print("Before")
        val = func()
        # do something after
        print("After")
        return val
    return wrapper

@logtime       # hello = logtime(hello)
def hello():
    print("Hello")
    
hello()