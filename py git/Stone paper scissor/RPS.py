import random
import time
player = input(" Select one from 'Stone' 'Paper' 'Scissor' : ")
while True :
    
    
    computer = random.choice(['Stone', 'Paper', 'Scissor'])
    time.sleep(2)

    if player == computer:
        print("TIE! Computer reads your mind")
    elif player == "Stone":
        if computer == "Paper":
            print("You Lose", computer,"covers",player)
        else:
            print("WoW! You Win -",player, "smashes",computer)
    elif player == "Paper":
        if computer == "Scissor":
            print("Sorry You Lose", computer,"cuts",player)
        else:
            print("WoW! You Win -",player, "covers", computer)
    elif player == "Scissor":
        if computer == "Stone":
            print("You Lose", computer, "smashes", player)
        else:
            print("You Win -",player, "cuts", computer)
    else:
        print("Choose Properly")

        
    NextGame = input("Play Again? (yes or no)")
    if NextGame == "yes":
        player = input(" Select one from 'Stone' 'Paper' 'Scissor' : ")
    else:
        break

print("See You Soon")
                   
