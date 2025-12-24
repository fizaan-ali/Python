import time
# time.perf_counter() -> gives us time from fixed starting point !!
# the alone value didn't important the difference is important
# it tells us how much time did some task take to perfrom 
# in one program, uses one continuous clock
# both start and end come from the same clock

start = time.perf_counter()  # gives us some time 

def counter(num):
    count = 0
    while count < num:
        count += 1
    print(count)

counter(1000000000)

end = time.perf_counter() # the same counter gives us time after 

print("Time elapsed to count", end-start, "secs") # now the difference tells us how much time it is taking to excute the block of code between start and end 


# now this is the output 
# it means it itakes about 159 seconds for cpu to count from 0 to 1000000000

# PS C:\Users\Fizaan\Desktop\Python> python -u "c:\Users\Fizaan\Desktop\Python\sample.py"
# 1000000001
# Time elapsed to count 158.94854250000208 secs