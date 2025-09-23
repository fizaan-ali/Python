def greet(name, ending = "Thank you!"): # ending --> by defualt parameter if value provided then will print according to it otherwise print the default value if not provided in argument
    print(f"Good Day, {name}.")
    print(ending)

greet("Fizaan")

greet("Areeb", "Nice meeting you.")

