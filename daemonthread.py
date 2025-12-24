# daemon thread -> a thread that runs in the background, not important for program
#           to run.. Your program will not wait for the daemon threads to 
#           complete before exiting. 
#           Non daemon threads cannot normally be killed, stay alive until task is complete
#           ex. background tasks, garbage collection, waiting for input, long running process

# import threading
# import time

# def timer():
#     print()
#     count = 0
#     while True:
#         time.sleep(1) # sleep for 1 sec
#         count += 1
#         print("Logged in for ", count, "seconds")
        
# x = threading.Thread(target=timer) # now this is normal thread / non-daemon # the problem is start it's not going to be killed/ terminate when our main thread have finsished it's job it's going to do that's where we use daemon threads
# x.start()

# answer = input("Do you want to exit? ")

# now below is the output of the above program 

# Do you want to exit? Logged in for  1 seconds
# Logged in for  2 seconds
# Logged in for  3 seconds
# Logged in for  4 seconds
# Logged in for  5 seconds
# Logged in for  6 seconds
# Logged in for  7 seconds
# ok
# Logged in for  8 seconds
# Logged in for  9 seconds
# Logged in for  10 seconds
# Logged in for  11 seconds
# Logged in for  12 seconds


# now daemon tasks are killed automatically when our non- daemon tasks are finished !!

import threading
import time

def timer():
    print()
    count = 0
    while True:
        time.sleep(1) # sleep for 1 sec
        count += 1
        print("Logged in for ", count, "seconds")
        
x = threading.Thread(target=timer, daemon=True) # to make a thread daemon = True we put daemon in argument
x.start()

answer = input("Do you want to exit? ")

# now this is its output
# Do you want to exit? Logged in for  1 seconds
# Logged in for  2 seconds
# Logged in for  3 seconds
# Logged in for  4 seconds
# Logged in for  5 seconds
# Logged in for  6 seconds
# Logged in for  7 seconds
# ok


# x.setDaemon(True) # sets our thread to daemon (make sure it's not start yet)
print(x.isDaemon()) # checks if x is Daemon or not
