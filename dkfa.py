import os
directory_path = 'c:/users/fizaan/desktop/python'
contents = os.listdir(directory_path)
for item in contents:
    print(item)