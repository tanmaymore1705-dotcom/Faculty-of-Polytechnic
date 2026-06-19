#problem1
def countdown(n):
    while n >= 1:
        print(n)
        n = n - 1
    print("Liftoff!")

countdown(5)

#problem2
def first_multiple(n, start):
    x = start
    while True:
        if x % n == 0:
            break
        x = x + 1
    return x

print(first_multiple(5, 12))

#problem3
def print_triangle(height):
    row = 1
    while row <= height:
        print("*" * row)
        row += 1

print_triangle(5)

#problem4
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

print(is_prime(7))   # True
print(is_prime(10))  # False

#problem5 - guessing game
import random

def play_game():
    secret = random.randint(1, 100)
    tries = 0
    while True:
        guess = int(input("Guess the number (1-100): "))
        tries += 1
        if guess < secret:
            print("Too low!")
        elif guess > secret:
            print("Too high!")
        else:
            print(f"Correct! You guessed the number in {tries} tries.")
            break

play_game()

#problem8 - D13 scope fix
def add_item(running_total, price):
    return running_total + price

def apply_tax(cart_total):
    return cart_total * 1.05

def main():
    total = 0
    total = add_item(total, 40)
    total = add_item(total, 25)
    total = add_item(total, 15)
    print(f"Items added. Cart total: {total}")
    print(f"With 5% tax: {apply_tax(total):.2f}")

if __name__ == "__main__":
    main()
