# RECURSION

def factorial(n):
    if n==1: # base case
        return 1
    return n * factorial(n-1)

n = int(input("Enter the number: "))
print(f"Factorial is: {factorial(n)}")