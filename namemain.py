# Module can be run as standalone program
# Module can be imported and used by other modules

# Python interpreter sets 'special variables', one of which is '__name__'
# then python will execute the code found within main

# Python will assign the __name__ variable a value of '__main__' if it's the 
# initial module being run!!!!

# if __name__ == '__main__'

import samplemodule

# print(__name__) # prints '__main__' # now this '__name__' is this module variable it will print the __main__ bcz this is the main module running
# print(samplemodule.__name__) # prints 'samplemodule' # now if we print the '__name__' for other module being imported it will bring the module name!

# why need this ?? 
# the real problem is python executes everything inside a module that is being imported
# now this is the problem we don't want that 
# and then we put all of the code into the main() function and then write 
# this condition as if name = main then and only then execute this function 
# otherwise not 

#ok gottcha so we use this to stop the module code starts executing so it is there in our file but just a piece of writing not executing anything we write it in our code so that while this file is being imported it won't start executing automatically



# we write like this 
# if __name__ = '__main__': # if the module is our main function 
#   main() # only then run our main file 
