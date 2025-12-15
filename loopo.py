num = int(input("Enter the number: "))

print(f"Below is a multiplication table for {num}: \n")

for i in range(1, 11, 1):
    
    print(f"{num} * {i} = {num * i}")

else:
    
    print("Done printing the multiplication table!")

