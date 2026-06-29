#problem
SECRET = 10

def play_game():
    guesses = 0

    while True:
        guess = int(input("Enter your guess: "))
        guesses =+1

        if guess > SECRET:
            print("Too high!")
        elif guess < SECRET:
            print("Too low!")
        else:
            print(f"Correct! You got it in {guesses} tries.")
            break

play_game()
