import time

print(time.ctime(0)) # starting point  # convert a time expressed in seconds since epoch to a readable string
                # epoch -> when our computer thinks time began (reference point)
# ctime(seconds) # now it will give us the time after seconds pass since epoch
# ctime(86400) # now this will give us the time one day after epoch # now you know

# ctime(1000000000)

print(time.time()) # return current seconds since epoch # uses system clock

print(time.ctime(time.time())) # gives us current data and time  -> based on above two 

time_object = time.localtime()
print(time_object) # now this is not readable
# this is the output of the above line of code
# time.struct_time(tm_year=2025, tm_mon=12, tm_mday=23, tm_hour=22, tm_min=3, tm_sec=45, tm_wday=1, tm_yday=357, tm_isdst=0)


# to format time object

local_time = time.strftime('%B %d %Y %H:%M:%S', time_object) # there are many formats available you can see in onlinepr

print(local_time)


# we can also get coordinated universal time or UTC we use time.gmtime() func for this

time_string = "20 April, 2025"
time_object = time.strptime(time_string, "%d %B, %Y") # now this will create a time object from the format which we give it to it first we will tell him what is this what is that

print(time_object)