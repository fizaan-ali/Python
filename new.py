import random

def game():
    print("Playing the game.........")
    score = random.randint(1,50)
    # Fetch the hiscore!
    with open("hiscore.txt", "r") as file:
        hiscore = file.read()
        if(hiscore != ""):
            hiscore = int(hiscore)
        else: 
            hiscore = 0
        
    print("Your score is : ", score)
    # Write the hiscore!
    if(score > hiscore):
        with open("hiscore.txt", "w") as file:
            file.write(str(score))
    return score
    
game()