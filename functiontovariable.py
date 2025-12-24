def hello():
    print("Hello")

 # all things in python are objects!

hello # now it is an object in a memory location in python
print(hello)

hi = hello # now we are pointing hi to the same memory location as is hello

hi() # now if we do hi() it will call that function() that hello() is bcz both hi and hello are poiting to same object(function)
# kinda like alias

# also to built-in

say = print

say("Say my name!") # it will act like same print() function!!
say("Fizaan Ali")