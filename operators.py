1 + 1 #2 --> addition
2 - 1 #1 --> subtraction
3 * 6 #18 --> multiplication
2 / 2 #1 --> divison
4 % 3 #1 --> remainder
2 ** 5 #32 --> exponents (power)
5 // 2 #2  --> floor divison means 5 / 2 = 2.5 and rounds to lower integer (2)

# is, in --> these are also the operators in python
# Ternary operator
def is_adult(age):
    if age > 18:
        return True
    else:
        return False

def is_adult2(age):
    return True if age > 18 else False # this is ternary operator