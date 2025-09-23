n = int(input("Enter the number: "))
def m_table():
    print("Below is the multiplication table for the number: ")

    for i in range(1,11):
        print(f"{n} X {i} = {n*i}")

def factorial(): # --> Function Definition
    print("Here is the factorial for the number: ")
    product = 1
    for i in range(1,n+1):
        product = product * i
    print("\tFactorial: ", product)

factorial()  # --> Function Call
m_table()