# logical operators (and, or, not) = used to check if two or more conditional statements are true

temperature = int(input("What is the temperatrue outside? "))

if temperature >= 0 and temperature <= 30: # if both are true then it's going to return true otherwise false
    print("The temperature is good today")
    print("Go outside!")
elif not(temperature > 0) or temperature > 30: # returns true if either one of the conditions is true
    print("The temperature is not good today")
    print("Stay Inside!")
     
# not -> flips true to false and false to true! 