# https://chatgpt.com/share/694b693d-620c-800c-bfdf-3bf93f772c8e
# multi-processing:
# running tasks in parallel on different cpu cores, bypasses GIL used for threading
# multi-processing -> better for cpu bound tasks (heavy cpu usage)
# multi-threading  -> better for io bound tasks (waiting around)

from multiprocessing import Process, cpu_count
import time

def counter(num): # a tuple!
    count = 0
    while count < num:
        count += 1

def main():

    print(cpu_count()) # no. of additional processes you can run # in my case 4!

# if we create more processes then cpu_count, it actually decreases our performace because then there's overhead of creating and destroying the processor we've given

    a = Process(target=counter, args=(100000000,))
    b = Process(target=counter, args=(100000000,))
    
#  now we split our task into multiple  cores -> so they finish up the task early!!!

    start = time.perf_counter()

    a.start()
    b.start()

    a.join() # main process will wait for 'a' process to finish
    b.join()

    end = time.perf_counter()

    print("Finsihed in", end-start , "seconds.")


if __name__ == '__main__': # only then run this program if its start running directly, if it's being imported (in child class) then not run it if we don't do this otherwise it will running this file again and again in childrenss!!!
                            # only in our this file it is main # but if we do multiprocessing our file is being imported and then it's not main # only one can be '__main__' at a moment
    main()


# so in this example we used multi-processing to finish up the task (counting) earlier

# output :

# PS C:\Users\Fizaan\Desktop\Python> python -u "c:\Users\Fizaan\Desktop\Python\multiprocessing_.py"
# Finsihed in 11.02181780000683 seconds.