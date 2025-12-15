# TRUE: // when is there something TRUE
# 1. True
# 2. Numbers are always true except 0
# 3. All non-empty strings

# FALSE: // when is there something FALSE
# 1. False
# 2. 0
# 3. Empty strings, lists, tuples, dict

done = "0"
if done:
    print("yes")
else:
    print("no")

#ANY -> checks if any of them is true if true then it's gonna return true otherwise false. 
print(any([True, 0, "", "Fizaan"])) #-> if any of them is true it's gonna return true
print(any([False, 0])) # returns false none of them is true

#ALL -> returns true if all of the values are true otherwise false
print(all([True, 0, ""]))
print(all([True, 1]))   