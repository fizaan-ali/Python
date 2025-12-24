website = "https://www.youtube.com"
website1 = "https://www.instagram.com"

# let's say we only want the webstie name not complete url
# slice(start, stop, step(optional))

slice = slice(12,-4) # creates a slice object  -> we use slice so we can reuse our logic 

# we did 12 -> bcz it's going to start with first char of website
# as website name is variable so we use negative slicing -4 so it's going to print before '.com'abs

print(website[slice])
print(website1[slice])