# to pass and use arguments via command line!
import sys

print(sys.argv) # it returns the list of arguments which are given in command line while running

# e.g., python arg.py Fizaan 55  (write in command line)
# it's gonna print --> ['arg.py', 'Fizaan', '55']

name = sys.argv[0]
print(name)