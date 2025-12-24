import random

while True: # keeps playing with user
    choices = ["rock", "paper", "scissors"]

    computer = random.choice(choices)
    player = None

    while player not in choices:
        player = input("Enter your choice (rock, paper, scissors): ").lower()
        if player not in choices:
            print("Enter only from 'rock', 'paper', 'scissors'")

    print(f"You chose: {player.capitalize()}, Computer chose: {computer.capitalize()}") # f string


    if player == computer:
        print("It's a Tie!")
    elif player == "rock":
        if computer == "paper":
            print("Computer won! You lose!")
        else:
            print("You won! Computer loses")
    elif player == "paper":
        if computer == "rock":
            print("You won! Computer loses")
        else:
            print("Computer won! You lose!")
    elif player == "scissors":
        if player == "rock":
            print("Computer won! You lose!")
        else:
            print("You won! Computer loses!")

    play_again = input("Play Again (yes/no) ?? ").lower()
    if play_again != "yes":
        print("Byeee")
        break
    