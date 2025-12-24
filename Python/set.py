# set = collection which is unordered, unindexed. No duplicate values!

# unordered means there is not any special order of values in the set, random, not any positional thing here!!

utensils = {"fork", "spoon", "knife", "spoon"}
dishes = {"bowl", "plate", "cup", "jug"}


utensils.add("napkin")
utensils.remove("fork")
# utensils.clear() # clear all the things in setttt
 
utensils.update(dishes) # adds everything in dishes to utensils


for x in utensils:
    print(x)

# print("knife" in utensils)
# print("spooon" in utensils)




s1 = {1,2,3,4,5,6}
s2 = {4,5,6,7,8,9}
# there are also several other set methods!!

print(s1.union(s2)) # s1 | s2 -> union of s1 and s2
print(s1.intersection(s2)) # s1 & s2 -> intersection of s1 and s2
print(s1.difference(s2)) # s1 - s2 -> difference of s1 and s2
print(s1.issubset(s2)) # is s1 a subset of s2?
print(s1.isdisjoint(s2)) # are they two completely different sets intersection is empty
