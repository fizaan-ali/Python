# scope = the region where that variable is recognized
#          a variable is avaialable only from the region it is created
#           a global and locally scoped versions of a variable can be created

name = "Ali" # global scope (available inside and outside of functions)

def display_name():
    name = "Fizaan" # local variable -> local to this funct only
    print(name)

display_name()
print(name)

# so inside some functin if there are same named local and global variables
# the function first use local variable and if not found with that name it's 
# going to use global vairable

# LEGB Rule:
# local, enclosed, global, built-in