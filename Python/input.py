# INPUT -> using the input() function!
name = input("What is your name? ") # inputs in the form of string always -> have to typecast to do others
age = input('What is your age? ') # takes age input as string
height = float(input("What is your height? "))

print("Hello " + name)
print("You will be " + str(int(age) + 1) + " years old next year!") # it will show error bcz we can't do addition with string and integer 
print("Your are " + str(height) + " cm tall")
# to do so we have to typecast age to integer
# age = int(input("What is your age? ")) # now age is int! only int not float
