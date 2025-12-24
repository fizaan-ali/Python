# zip(*iterables) -> aggregate elements from two or more iterables (list, tuples, sets)
#              creates a zip object with paired elements stored in tuples for each element

username = ["Fizaan", "Ans", "Abdullah"]
password = ("p@ssword", "abc123", "guest")


users = zip(username, password) # zip object is iterable # you can add many iterables!

print(type(users)) # can typecase to other iterables
users = dict(users)

for key,value in users.items():
    print(key + " : " + value)