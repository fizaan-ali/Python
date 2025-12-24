# if statement: a block of code that will execute if the condition is true!
age = int(input('How old are you? '))

if age >= 18:
    print("You are an adult!")
elif age >= 13:
    print("You are a teen!")
elif age >= 3:
    print("You are a child!")
elif age == 100:
    print("Why haven't you died yet!")
elif age < 0:
    print("You haven't been born yet!")
else:
    print("You are a baby!")


# now if we enter age 100 in input -> it would still print 'you are an adult' 
# despite 'you haven't been born ....' because it's going to check line by line 
# the first condition which matches our code is going to print else are going to be
# neglected. if none of them is going to match the else part would run
# SO ORDER MATTERS!!


# only one of the code block is going to run based on the condition!
# if none of the conditions match, the else block is going to run
