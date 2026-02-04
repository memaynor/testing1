import random

randnum = random.randint(1,10)
guess = int(input("Guess a number between 1-10: "))

if guess == randnum:
    print("Good Job! You guessed correct!")
else:
    print("Try again! The number was", randnum, ".")