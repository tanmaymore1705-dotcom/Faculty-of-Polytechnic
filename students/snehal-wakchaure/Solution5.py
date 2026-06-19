def print_triangle(height):
    for i in range(1, height + 1):
        print("*" * i)


print_triangle(5)


import random

prsonal = random.randint(1, 100)

print("guess num  1 & 100!")

while True:
    guess = int(input("guess: "))
    
    if guess < prsonal:
        print("T low!")
    elif guess > prsonal:
        print("T high!")
    else:
        break


SECRET = 10

def play_game():
    guesses = 0

    while True:
        guess = int(input("Enter your guess: "))
        guesses += 1

        if guess > SECRET:
            print("Too high!")
        elif guess < SECRET:
            print("Too low!")
        else:
            print(f"Correct! You got it in {guesses} tries.")
            break

play_game()
