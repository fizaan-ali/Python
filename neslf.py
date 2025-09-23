def generate_table(num):
    table = ""
    for i in range (1,11):
        table = table + f"{num} X {i} = {num*i}\n"
    with open(f"tables/table_{num}.txt", "w") as file:
        file.write(table)

for i in range(2,21):
    generate_table(i)
    