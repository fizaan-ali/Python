lis = [55, "Fizaan Ali", True, 20.3, "Ans", 0, 3.1415]
lis[2] = False
print(64 in lis) # returns true if given thing is in list

l1 = [] # empty list

print(lis[0]); print(lis[1])

print(lis[-1]) # negative indexing -1 for last one 

print(lis[1:4]) # print from index 1 to index 3 

lis.append("Ahsan") # appends only one element
lis.extend([51, "Suleman"]) # extends one iterable

lis += [90, "Saqib"] # extends  the list  -> same as extend

lis.remove(90) # deletes by value --> if not found gives error --> returns nothing

lis.pop() # deletes by index .pop(1) if no index is given delete last value --> returns the removed value 

lis.insert(2,"Ali") # inserts value at specific index 

lis[1:1] = [29] # to add multiple elements at specific index we use slicng
print(lis[1])
print(lis)
print(len(lis))


lis1 = [32, 35, 51, 54, 20, 100]

lis1copy = lis1

lis1.sort()

print(lis1)
print(lis1copy)


# shallow copy vs deep copy
lis = [1,2,3,4,5]
liscopy = lis[:]
lis[1] = 8
print(lis)
print(liscopy)

lis3 = [23,2,59]
print(sorted(lis3)) # does not alter exisitng list -> returns new sorted list
