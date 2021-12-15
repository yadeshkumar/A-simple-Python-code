import random as r

num = r.randrange(100)
guess = 5
while guess > 0:
    yourGuess = int(input("enter your guess"))

    def check(x):
        if yourGuess == x:
            print("You win")
        elif yourGuess > x:
            print("You are close, keep trying lower")
        else:
            print("Your are close, keep trying higher")

    if guess > 1:
        check(num)
    elif guess == 1:
        check(num)
        print ("this is your last chance")
    else:
        print("you lost")
    guess = guess - 1
