import random

print(random.random()) # gives a random floating point number between 0 and 1

x = random.randint(1,6) # gives random number btw two values # both values included
print(x)

# random.randrange(start, stop ,step(optional)) # gives a random number between some range we can also include step

print(random.randrange(1,10,)) # gives random number btw 1 and 10
print(random.randrange(0,20,2)) # gives random number btw 0,2,4,6,...,20

# random.choice(<sequence>) # picks one random item from a list, tuple, or string

picks = ["rock", "paper", "scissors"]
print(random.choice(picks))

# random.unifrom(a,b) # gives random float number between a and b

print(random.uniform(1.5, 4.9))

# random.shuffle() -> shuffles the elements in a list changes the orignal one
l = [1,2,3,4,5]
random.shuffle(l)
print(l)

# random.sample(sequence, k) -> returns a list of k unique items out of a sequence
name = "fizaan ali"
print(random.sample(name, 3)) # returns a list of 3 unique random things from a string(sequence)


