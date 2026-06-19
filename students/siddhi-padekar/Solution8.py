#solution8
import random

def guess_game():
    secret = random.randint(1, 10)

    while True:
        guess = int(input("Guess the number (1-10): "))

        if guess == secret:
            print("You win!")
            break
        elif guess < secret:
            print("Too low!")
        else:
            print("Too high!")

guess_game()
