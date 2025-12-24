# filter() -> creates a collection of elements from an iterable for which a function returns true

# filter(function, iterable)

friends = [("Fizaan", 17),
           ("Ans", 22),
           ("Shaheryar", 21),
           ("Hamid", 19),
           ("Husnain", 20),
           ("Areeb", 10),
           ("Ahmaed", 16)]

age = lambda data : data[1] > 18

adults = list(filter(age, friends))

print(adults)


# simple example

l = [1,2,3,4,5,6,7,8,9,10]

is_even = lambda x : x % 2 == 0 # we can also do this using functions but this is simpler

print(list(filter(is_even, l)))