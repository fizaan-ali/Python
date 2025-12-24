# copyfile() -> copies content of a file
# copy() -> copyfile() + permission mode + destination can be a directory
# copy2() -> copy() + metadata() (file's creation and modification times)

import shutil

shutil.copyfile('test.txt', 'copy.txt') # src, dest 
# also we can pass source and destination addresses in it 


# shutil.copy(src, dstn)