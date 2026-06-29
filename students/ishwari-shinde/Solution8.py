#problem 1
#triangle range
def print_triangle(h):
    for i in range(1, h + 1):
        print("*" * i)
print_triangle(5)

#problem 2
#countdown
def countdown (n):
    while n >=1:
        print(n)
        n-=1
     print("liftoff!")
countdown (5)


#problem 3
#play game


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


