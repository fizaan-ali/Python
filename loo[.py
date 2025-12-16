# LOOPS: WHILE & FOR LOOOPS

num = 1
while num <= 10:
    print(num)
    num += 1

print("helllo there after the loop")

# for loop -> iterates over a sequence of objects picks one item do required taks then go over to the next item unless none left!
items = [1,2,3,4]
for item in items:
    print(item)


print(list(range(2,10,2)))
# range function range(start, stop, step) !stop one is mandatory!
# it creates a sequence of iterable numbers 

for i in range(15):
    print(i)


names = ["Fizaan", "Ali", "shafiq"]
for index, name in enumerate(names):
    print(index, " ", name)

print(list(enumerate(["Fizaan", "ali", "shafiq"])))