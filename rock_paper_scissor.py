'''
1 for Rock
0 for Paper 
-1 for Scissors

Rock vs Paper --> Paper wins
Paper vs Scissors --> Scissors wins
Rock vs Scissors --> Rock wins
'''
import random
computer = random.choice([0,1,-1])

youstr = input("Enter your choice: ")
you_str = youstr.lower()
you_dict = {
    "rock" : 1,
    "paper" : 0,
    "scissors" : -1
}
you = you_dict[you_str]
reversed_dict = {
    1 : "Rock",
    0 : "Paper",
    -1 : "Scissors"
}
print(f"You chose {reversed_dict[you]}.")
print(f"Computer chose {reversed_dict[computer]}.")

if(computer == you):
    print("Its a tie!")
else:
    if(computer == -1 and you == 0): # rock, paper, scissors --> 1, 0, -1
        print("You lose")
    elif(computer == -1 and you == 1):
        print("You win")
    elif(computer == 0 and you == 1):
        print("You lose")
    elif(computer == 0 and you == -1):
        print("You win")
    elif(computer == 1 and you == 0):
        print("You win")
    elif(computer == 1 and you == -1):
        print("You lose")
    else:
        print("Something went wrong.")

