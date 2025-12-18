expenses = [("Dinner", 80), ("Car", 120)] # list of tuples
# now if you want to calculate the sum of expenses
sum = 0
for expense in expenses:
    sum += expense[1]
print(sum)