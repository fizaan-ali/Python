# "string"
# 'string'
# "Fizaan"
# name = "Fizaan" + " Ali"
# name += " is my name"
# print(name)


# str1 = "I am Fizaan Ali"
# # triple quoted (eiher single or double) -> multiline 
# str2 = """I  
#         am 
#         Fizaan 
#         Ali """

# print(str2)

print("Fizaan ali".upper())
print("FizAAn ali".lower())
print("fizaan ali".title())

# --> all the string methods return new altered string they don't alter the existing string

name = "FizAAn AlI"
new = name.upper()
print(f"This is original one: {name}")
print(f"This is new one: {new}")

print("fizaan".startswith("f"))
print("fizaan".endswith("aai"))
print(len(name))
print("an" in name) # if there is substring in a string return true otehrwise false