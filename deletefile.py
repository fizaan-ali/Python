import os
import shutil

path = 'empty_folder'

try:
    # os.remove(path) # it doesn't remove a folder
    os.rmdir(path) # this is how to remove an empty directory/ -> it won't remove folder with files
    # shutil.rmtree(path) # delete the directory and all files in that directory
except FileNotFoundError as e:
    print(e)
    print("That path was not found!") 
except PermissionError as e:
    print(e)
    print("You do not have permission to delete that")
except OSError:
    print("You can't delete that using that function")
else:
    print("'" + path + "'" + " was deleted") 