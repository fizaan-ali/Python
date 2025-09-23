'''
1 for snake    
0 for water 
-1 for gun
'''
'''
if both are same --> tie
snake vs water --> snake wins
water vs gun --> water wins
snake vs gun --> gun wins
'''
import random
computer = random.choice([1,0,-1])

youstr = input("Enter your choice: ")
youdic = {
    "s" : 1, 
    "w" : 0,
    "g" : -1
}
you = youdic[youstr]

reverse_dic = {
    1 : "Snake",
    0 : "Water",
    -1: "Gun"
}
print(f"You chose {reverse_dic[you]}.")
print(f"Computer chose {reverse_dic[computer]}.")

if( computer == you ):
    print("Its a tie!")
else:
    if(computer == -1 and you == 0): # -1
        print("You win!")
    elif(computer == -1 and you == 1): # 0
        print("You lose")
    elif(computer == 0 and you == 1):  # 1       # -1 --> gun
        print("You win!")                        #  0 --> water 
    elif(computer == 0 and you == -1):  # -1     #  1 --> snake
        print("You lose")
    elif(computer == 1 and you == 0): # 1
        print("You lose")
    elif(computer == 1 and you == -1): # 0
        print("You win!")
    else:
        print("Something went wrong!")

# also we can shorten the if else ladder by finding some 
# similaritie between lose and win and write that 