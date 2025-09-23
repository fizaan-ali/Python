# # # sum of first n natural numbers using recursion
# # '''
# # 1 = 1
# # 2 = 2 + 1 
# # 3 = 3 + 2 + 1
# # 4 = 4 + 3 + 2 + 1
# # .       .
# # .       .
# # .       .
# # n = n + sum_(n-1)
# # '''
# # def sum_(n):
# #     if (n == 1):
# #         return 1
# #     return n + sum_(n-1)

# # n = int(input("Enter the number: "))

# # print(f"The sum of first {n} natural numbers is : {sum_(n)}.")

# # print("Hello there, ", end="") # end="" is used to remove the by default new line of print() function.
# # print("My name is Fizaan.")

# #Greatest of three numbers?
# def greatest(n1, n2, n3):
#     if(n1>n2 and n2> n3):
#         largest = n1
#     elif(n2>n1 and n2>n3):
#         largest = n2
#     else: 
#         largest = n3
#     return largest

# n1 = int(input("Enter the number: "))
# n2 = int(input("Enter the number: "))
# n3 = int(input("Enter the number: "))

# print(f"The largest number is : {greatest(n1, n2, n3)}.")


# Celsius to Fahrenheit

# def cel_fah(cel):
#     fah = (9/5) * cel + 32
#     return fah

# cel = float(input("Enter the temperature in celsius: "))
# print(f"Temperature in fahrenheit = {cel_fah(cel)}.")

# def func(n):
#     for i in range(1, n+1): # for i in range(n, -1, -1)
#         print("*" * (n+1-i)) # print("*" * i)
    
# n = int(input("Enter the number: "))
# func(n)
'''
1 --> 3 --> 4 --> 4 - i
2 --> 2 --> 4 ---> 4 - i
3 --> 1 --> 4 --> 4 - i
'''
# Inches to Centimetre --> 1 inch = 2.54 centimetre
# def in2cm(inch):
#     cm = inch * 2.54
#     return cm

# inch = float(input("Enter the no. of inches: "))

# print(f"The equivalent length in cm is : {in2cm(inch)}")

# def m_table(num):
#     for i in range(1, 11):
#         print(f"{num} X {i} = {num*i}")

# n = int(input("Enter the number: "))
# m_table(n)

list = [1,4,"ali", 3,4.13]

        