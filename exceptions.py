# EXCEPTIONS 
# way to handle errors!
# try:
#     # some lines of code
# except <ERROR1>:
#     # handler <ERROR1>
# except <ERROR2>:
#     # handler <ERROR2>
# else:
#     # no exceptions were raised, code run successfully
# finally:
#     # do something in any case!!

try:
    result = 2/0
except ZeroDivisionError:
    print("Cannot divide by zero!")
finally: # always going to run if there's any error or not 
    result = 1

print(result) # 1


raise Exception("An error!!")

try:
    raise Exception("An error occurred")
except Exception as error:
    print(error)


class NotFound(Exception): # we can also create own exception by using this 
    print("inside exception")
    

try:
    raise NotFound()
except NotFound:
    print("The thing not found")