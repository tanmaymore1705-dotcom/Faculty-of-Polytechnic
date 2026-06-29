#problem 1

n=int(input("enter your number="))
def countdown(n):
    while n>=1:
        print(n)
        n=n-1
    print("Liftoff!")
countdown(n)

#problem 2

def print_triangle(height):
    row=1
    while row<=height:
        print("*"*row)
        row=row+1
print_triangle(10)

#problem 3
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
