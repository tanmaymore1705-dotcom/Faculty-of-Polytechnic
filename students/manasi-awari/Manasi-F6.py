secret = 42
tries = 0

while True:
    guess = int(input("Guess the number (1-100): "))
    tries += 1

    if guess > secret:
        print("Too high!")
    elif guess < secret:
        print("Too low!")
    else:
        print(f"Correct! You got it in {tries} tries.")
        break
