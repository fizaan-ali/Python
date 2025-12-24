# str.format() = optional method that gives users more control when displaying output!

animal, item = "cow", "moon"

# print("The " + animal + " jumed over the " + item)

print("The {} jumped over the {}".format(animal, item)) 
print("The {1} jumped over the {0} and {1} is beautfiul".format(animal, item)) # positional arguments

# in this they use indexing for things aftinside .format() 
# the default sequence is this . 0,1,2,3..... but we can also change it as above!!
# {1} value at index 1 {0} value at index 0
# also reuse values using same index

# # {} -> format fields / placeholders for things, variables
# sequence matters!!!!



print("The {item} jumped over the {animal} and {animal}".format(animal="cow", item="moon")) # keyword arguments
# for this, we also don't need variables that we've above created!!
# also reuse the argumentss!


text = "The {} jumped over the {}"

print(text.format(animal, item))








name = "Fizaan"
print("Hello, my name is {}".format(name))
# we can also add padding

print("Hello, my name is {}. Nice to meet you!".format(name)) # no padding
print("Hello, my name is {:10}. Nice to meet you!".format(name)) # left align # now name will occupy ten character space
print("Hello, my name is {:<10}. Nice to meet you!".format(name)) # left align
print("Hello, my name is {:>10}. Nice to meet you!".format(name)) # right align
print("Hello, my name is {:^10}. Nice to meet you!".format(name)) # center align

#if there's positional or keywrod argument now then how to add
# print("Hello, my name is {0:>10}. Nice to meet you!".format(name))
# print("Hello, my name is {name:^10}. Nice to meet you!".format(name="Fizaan"))


number = 3.14159
number_ = 10000

print("The number pi is {}".format(number))
print("The number pi is {:.3f}".format(number)) # this will round the numbers
print("The number pi is {:.2f}".format(number)) # rounds upto 2 decimal digits
print("The number is {:,}".format(number_)) # adds comma at thousands field
print("The number is {:b}".format(number_)) # convert to binary
print("The number is {:o}".format(number_)) # convert to octal
print("The number is {:x}".format(number_)) # convert to hexadecimal x for small X for large
print("The number is {:e}".format(number_)) # convert to scientific notation e for small E for large



