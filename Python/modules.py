# module = a file containing python code. May contain functions, classes, etc. 
# used with modular programming which is to separated program into parts


# this will import all the contents in greet.py file in the same directory # also we can specify the lcoation

# import greet 
# greet.hello()
# greet.bye()

# we can also give alias / nickname to our moduel
# import greet as g

# g.hello()
# g.bye()


# also we can specify the contents importing from file!

from greet import hello, bye
hello() # no need to then write greet. before!
bye()

# from greet import * -> import all the things!