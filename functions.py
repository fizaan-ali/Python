# FUNCTIONS 

def hello():
    print("Hello there, how are you?")
hello()
hello()
hello()

def hi(name):
    print(f"Hi {name}. How are yoU?")
hi("fizaan")
hi("areeb")

# Arguments -> values we pass during function call
# Parameters -> things that are in function definition inside parenthesis

# so then how to make argument option? like how to make default value if not passed by user
# def hello(name="my friend"):
#     print(f"Hello {name}! How are you?")
# hello()
# hello("fizaan")

# NESTED FUNCTIONS -> function inside another function

def count():
    count = 0
    def increment():
        nonlocal count
        count = count + 1
        print(count)
    increment()

count()
print(increment())