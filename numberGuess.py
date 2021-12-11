import random

max = 10

n = random.randint(1, max)
print("Welcome to guess the number game!")
print("Guess the number from 1 to %d" %max)
guess = None
while guess != n:
    guess = int(input("Your try: "))
    if guess > n:
        print("Too high")
    if guess < n:
        print("Too low")
print ("Congratulation, you WON")
