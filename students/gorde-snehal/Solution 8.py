#Guess number 
SECRET = 42

def play_game():
    guesses = 0

    while True:
        guess = int(input("Guess the number (1-100): "))
        guesses += 1

        if guess > SECRET:
            print("Too high!")
        elif guess < SECRET:
            print("Too low!")
        else:
            print("Correct! You got it in", guesses, "tries.")
            break

play_game()
