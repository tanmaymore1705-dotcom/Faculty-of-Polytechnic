 #problem 1
num = 10 
while True:
    guess = int(input("Guess a number between 1 and 20: "))
    if guess == num:
        print("Right")
        break  # FIX(faculty): added break so the loop stops on a correct guess (was an infinite loop)
    else:
        print("Wrong")

#problem 2
num = 10  # FIX(faculty): dedented to column 0 (the leading spaces caused an IndentationError)

while True:
    guess = int(input("Guess a number between 1 and 20: "))

    if guess == num:
        print("Right")
        break
    else:
        print("Wrong")
