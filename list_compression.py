# LIST COMPRESSION -> way to create lists in a very concise way!
numbers = [1,2,3,4,5]

numbers_square = [n**2 for n in numbers] # one line way of doing it alsooo

print(numbers_square)



# this is how you would do with a loop (long method)
# numbers_power2 = []
# for n in numbers:
#     numbers_power2.append(n**2)

# print(numbers_power2)

numbers_squre_2 = list(map(lambda n: n**2, numbers))