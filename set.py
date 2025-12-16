# SETS  -> Only distinct values -> ordered 
set1 = {"Fizaan", "Ali", "Shafiq"}
set2 = {"Fizaan"}
print(set1.intersection(set2)) # print(set1 & set2)

print(set1.union(set2)) # print(set1 | set2)

print(set1.difference(set2)) # print(set1 - set2)

print(set1.issuperset(set2))

print(set2.issubset(set2))

print(list(set1)) 

print("Shafiq" in set2)


s1 = {4,3,2,1}
print(s1) # would print it in ordered way!