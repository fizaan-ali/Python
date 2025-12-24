# Lamba Function -> function written in 1 line using 'lambda' keyword
# accepts any number of arguments but only has one expression
# (useful if needed for a short period of time)

# lambda parameters : expression

# def double(x):
#     return x*2
# print(double(4))

double = lambda x : x * 2
# print(result(4))
multiply = lambda x, y : x * y # takes two arguments x and y and returns their product
# print(multiply(3,6))
add = lambda x,y,z : x + y + z 
# print(add(1,2,3))
full_name = lambda first_name, last_name : first_name + " " + last_name
# print(full_name("Fizaan", "Ali"))
age_check = lambda age : True if age >= 18 else False # ternary operator
# print(age_check(17))

