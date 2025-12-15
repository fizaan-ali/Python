# def greet(name, ending):
#     print("Good Day, "+ name)
#     print(ending)

# greet("Fizaan", "Nice to meet you!")

# greet("Areeb", "Wonderful meeting!")

def factorial(num):
    product = 1
    for i in range(1,num+1):
        product = product * i
    return product

n = int(input("Enter the number: "))

print(f"Factorial of {n} = {factorial(n)}.")