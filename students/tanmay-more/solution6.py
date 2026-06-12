#problem no 1
num = 10

while True:
    guess = int(input("Guess a number between 1 and 20:"))

    if guess == num:
        print("Right")
        break
    else:
        print("Wrong")
