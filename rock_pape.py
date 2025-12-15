import random

def get_choices(): 
    player_choice = input("Enter a choice (rock, paper, scissors): ")
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)
    choices = {"player" : player_choice, "computer" : computer_choice}
    return choices

def check_win(player, computer):
    #print("You chose: " + player + ", Computer chose: " + computer)
    print(f"You chose: {player}, Computer chose: {computer}")
    if player == computer:
        return "Its a tie!"
    elif player == "rock":
        if computer == "paper":
            return "You lose."
        else:
            return "You win!"
    elif player == "paper":
        if computer == "rock":
            return "You win!"
        else:
            return "You lose!"
    elif player == "scissors":
        if computer == "paper":
            return "You win!"
        else:
            return "You lose."
 
choices = get_choices()
p_choice = choices["player"]
c_choice = choices["computer"]
result = check_win(p_choice, c_choice)
print(result)