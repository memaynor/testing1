import random

randnum = random.randint(1,10)
guess = int(input("Guess a number between 1-10: "))

if guess == randnum:
    print("Good Job! You guess correct!")
else:
    print("Try agian! The number was", randnum)