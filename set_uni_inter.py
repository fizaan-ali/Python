# s1 = {1,2,4,5,7}
# s2 = {2,3,5,6,8,7}

# print(s1.union(s2))
# print(s1 | s2)

# print(s1.intersection(s2))
# print(s1 & s2) 

# s1 = {1,2}
# s2 = {1,2,3}

# print(s1.issubset(s2))
# print(s2.issuperset(s1))
# print(s1.issuperset(s2))
# print(s1.isdisjoint(s2))

s1 = {1,2}
s2 = {3,4}
print(s1.isdisjoint(s2))

s1.clear() # clears the set 
print(s1)