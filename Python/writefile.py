text = "This is Fizaan Ali\nWhat are you doing?\nThis is so much fun!!\n"
# text_ = "Hello "
with open('test.txt', 'w') as file:  # by default the second argument is 'r'
    file.write(text) 

# it will overwrite the data in the file means all previous data in the file will be deleted!!!

# there is also 'a' append mode for writing at the end of the file

text_ = "Have a good day!"
with open('test.txt', 'a') as file:
    file.write(text_)