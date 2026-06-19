def play_game():
    SECRET = 7  
    tries=0
    while True:
        guess =int(input("Enter your guess: "))
        tries=tries+1
        if guess > SECRET:
            print("Too high!")
        elif guess < SECRET:
            print("Too low!")
        else:
            print("Correct! you got it in ",tries,"tries")
play_game()
