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
