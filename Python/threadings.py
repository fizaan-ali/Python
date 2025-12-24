# thread = a flow of execution. like a separate order of instructions
#          however each thread takes a turn running to achieve concurrency
#          GIL = (global interpreter lock), 
#           allows one thread to hold the control of Python interpreter  

# cpu bound = program/task spends most of its time waiting for internal events (CPUt intensive)
#               use multi processing

# io bound = program/task spends most of its time waiting for external events (user input, web scraping) 
#               use multi threading
import time
import threading

print(threading.active_count()) # active threading count

# def eat_breakfast():
#     time.sleep(3)
#     print("You finished breakfast")
# def drink_coffee():
#     time.sleep(4)
#     print("You finsished coffee")
# def study(): 
#     time.sleep(5)
#     print("YOu finished study")

# eat_breakfast()
# drink_coffee()
# study()

# now in the above case they are running sequentially (and takes about 15 secs) 
# bcz when one function ends only then is going to execute 
# but realistically humanns can multitask they can perform all three fucntions at the sametime 

def eat_breakfast():
    time.sleep(3)
    print("You finished breakfast")
def drink_coffee():
    time.sleep(4)
    print("You finsished coffee")
def study(): 
    time.sleep(5)
    print("YOu finished study")

x = threading.Thread(target=eat_breakfast, args=())
x.start()

y = threading.Thread(target=drink_coffee, args=())
y.start()

z = threading.Thread(target=study, args=())
z.start()

print(threading.active_count()) # active threading count # s0 now a total of 4 threads one main and the other three(x,y,z) are going to work

x.join() # -> now our main thread has to wait till our x thread will done completely his work to do his(main) other tasks

# so now all of the three functions will going to run simultaneously on diff threads so it's going to take less time 
y.join() # main thread will pasue until y completes its work

z.join() 
print("All tasks finsihsed successfully!")
