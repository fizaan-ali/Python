# reduce() -> apply a function to an iterable and reduce it to a single commulative value
#           performs action on first two elements and repeats until 1 value remains!

# reduce(function, iterable)

from functools import reduce # have to import it 

letters = ["F", "I", "Z", "A", "A", "N"]

word = reduce(lambda x, y: x + y ,letters)
# in this lambda function lambda x, y: x + y 
# it's going to take first two elements of iterable and performs the requried func (concatenation which is in this case)
# and then it's again going to repeat until one value remains 
# in second case the first value is going to be the previous result and second value is next value in iterable

print(word)

# Step 1: x = "F", y = "I"      → "FI"
# Step 2: x = "FI", y = "Z"    → "FIZ"
# Step 3: x = "FIZ", y = "A"   → "FIZA"
# Step 4: x = "FIZA", y = "A"  → "FIZAA"
# Step 5: x = "FIZAA", y = "N" → "FIZAAN"



# simple example
from functools import reduce

l = [1,2,3,4,5,6]

sum = lambda x, y : x + y 

print(reduce(sum, l))
