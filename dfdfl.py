# word = "Donkey"

# with open("donkey.txt") as file:
#      str = file.read()
# new_str = str.replace(word, "####")

# with open("donkey.txt", "w") as file:
#      file.write(new_str)

# Also for list of words

words = ["Donkey", "ganda", "bad", "dirty"]

with open("donkey.txt") as file:
    str = file.read()

for word in words:
    str = str.replace(word, "#" * len(word))
with open("donkey.txt", "w") as file:
    file.write(str)