# dictionary =  A changeable collection of unique key, value pairs 
#               fast because hashing, allow us to qucickly access a value!

capitals =  {'USA' : 'Washington Dc',
            'India' : 'New Delhi',
            'Pakistan' : 'Islamabad',
            'China' : 'Beijin',
            'Russia' : 'Moscow'
            }
print(capitals['Russia'])
# print(capitals['Germany']) # now if the key is not in dict. it is going to give error if we use this method
print(capitals.get('Germany')) # if the key is not in dict. it is going to return None

print(capitals)
print(capitals.keys())
print(capitals.values())
print(capitals.items()) # list of tuples of key value pairss

for key, value in capitals.items():
    print(key, value)



# dictionaries are changeable
capitals.update({'Germany' : 'Berlin'})
capitals.update({'USA' : 'London'})
capitals.pop('USA')
capitals.clear()
