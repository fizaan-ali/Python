# nested loop: the 'inner' loop will finish all of its iterations before finishing
# one iteration of the 'outer' loop!!!!!

# print a rectangle
rows = int(input("Enter the no. of rows: "))
cols = int(input("Enter the no. of columns: "))
symbol = input("Enter a symbol to use: ")

for i in range(rows):
    for j in range(cols):
        print(symbol, end="")
    print() # for new line after each row


