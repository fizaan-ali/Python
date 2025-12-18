# MODULES
# the dog is in the same folder!
import dog # import all the things from dog
dog.bark()

from dog import bark # import only bark from dog
bark()

# if dog is in subfolder

from lib import dog # import all the contents in dog

dog.bark()

from lib.dog import bark # import bark from dog (in lib)

bark()

#there are many built-in modules in the standard python library!
import math 

print(math.sqrt(16))

from math import sqrt

print(sqrt(15))