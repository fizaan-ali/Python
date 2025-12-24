# map() -> applies a function to each item in an iterable (list, tuple ..)

# map(function, iterable)

store = [("shirts", 20), # price in dollars
         ("pants", 25),
         ("jackets", 40),
         ("socks", 2)]
# now convert all to pkr

to_pkr = lambda data : (data[0], data[1] * 280)

store_pkr = map(to_pkr, store)
 
print(list(store_pkr))


# simple example

l = (1,2,3,4,5,6)

sq = lambda x : x * x

print(list(map(sq, l)))

