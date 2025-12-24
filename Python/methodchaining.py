# method chaining -> calling multiple methods sequentially 
#               each call performs an action on the same object and returns self

class Car:

    def turn_on(self):
        print("You turn on the engine")
        return self

    def drive(self):
        print("You drive the car")
        return self

    def brake(self):
        print("You applied the brakes")
        return self

    def turn_off(self):
        print("You turn off the engine")
        return self

car = Car()

# car.turn_on()
# car.drive()

car.turn_on().drive().brake().turn_off() 
# you can also write it like this 

# backslash '\' is a line continuation character it means the next things are in the same line you know what i'm saying
car.turn_on()\ 
    .drive()\
    .brake()\
    .turn_off()




# this is called method chaining 
# for method chaining the preceded function should return the arguments
# that a next function is taking parameters usually self
# e.g. in the above example drive method is taking self as parameter
# so the previous function turn_on() should then return self so it would go 
# to the next function as parameter and so on 
# otherwise the chainig won't work