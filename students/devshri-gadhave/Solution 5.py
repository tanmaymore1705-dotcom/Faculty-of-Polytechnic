#problem 1

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

#problem 2 

def print_triangle(height):
    for row in range(1, height + 1):
        print('*' * row)

# Example
print_triangle(5)

#problem 3

def countdown(n):
    while n > 0:
        print(n)
        n = n-1
    print("Liftoff!")

countdown(5)
