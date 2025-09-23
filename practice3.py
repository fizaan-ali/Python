# name = input("Enter your name: ")
# print(f"Good afternoon, {name}!")
letter = '''
Dear <|Name|>,
You are selected!
<|Date|>
'''
print(letter.replace("<|Name|>", "Fizaan").replace("<|Date|>", "20th June 2024"))

letter1 = '''
Dear <|Name|>,
You are selected!
<|Date|>
'''