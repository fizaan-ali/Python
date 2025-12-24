# slicing = creating a substring be extracting elements from another string
#   indexing[] or slice()
#   [start: stop: step]
#   step is optional 

name = "Fizaan Ali Shafiq"

first_name = name[0:6] # [:6]
last_name = name[11:17] # [11:]
funky_name = name[0:17:2] # takes 2 step # [::2]
reversed_name = name[::-1] # start backwards 

print(first_name)
print(last_name)
print(funky_name)





# [::] = [0:17:1] -> in case of name
# first_name = name[::] # the default values are [::] = [0:len(name):1] 

# print(first_name)
