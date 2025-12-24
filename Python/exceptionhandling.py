# exception = events detected during execution that interrupts the flow of program
try:
    numerator = int(input("Enter a number to divide: "))
    denominator = int(input("Enter a number to divide by: "))
    result = numerator/denominator
# except ZeroDivisionError :
#     print("You can't divide by zero, idiot!")
# except ValueError:
#     print("Enter only numbersssss!")

# except Exception: # very generic exception! if no one exception matches the error type it' gonna run
#     print("Something went wrong :(")


except ZeroDivisionError as e: # more formal way -> also print's what's exceptoin
    print(e)
    print("You can't divide by zero, idiot!")
except ValueError as e:
    print(e)
    print("Enter only numbersssss!")

except Exception as e: # very generic exception! if no one exception matches the error type it' gonna run
    print(e)
    print("Something went wrong :(")
else: # if no exception / error occurs, the else part is going to run # if exception found not going to run else part
    print(result)
finally: # always going to run if excepton occurs or not # good with file handling to close file at the end
    print("This will always execute")