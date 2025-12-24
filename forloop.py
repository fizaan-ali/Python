# for loop : a statement that will execute it's block of code for a limited number of times
#             --  for loop: limited, while loop: unlimited --

# range(start, stop, step) -> start and step are optional 
# stop is mandatory and by default start value is 0 and step value is 1.
# start is inclusive and stop is exclusive

# for i in range(10):
#     print(i+1)


# for i in range(50, 101, 2): # 50 - 99 -> first inclusive, second exclusive
#     print(i)

# we can iterate for loop with any iterable!! e.g. string, lists etc

# for i in "Fizaan Ali Shafiq Mughal":
#     print(i)

import time

for seconds in range(10, 0, -1):
    print(seconds)
    time.sleep(1)           # during each iteration; sleep for one second using time module!

print("HAPPY BIRTHDAY!!")  