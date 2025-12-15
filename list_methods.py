lists = ["Apple", "Banana", 5, 32.12, False, "Fizaan"]
print(lists)
lists.append(5) # adds an element to the end of the list
print(lists) # so it changes the original list unlike strings

l1 = [2,4,1,5,7,3,6]
# l1.sort() # sorts the list in ascending order
l1.reverse() # reverses the list
l1.insert(2, 100) # inserts 100 at index 2 
print(l1)

l2 = [1,3,5,7,9]
a = l2.pop(3) # removes and returns the element at index 3
print(a)
print(l2)