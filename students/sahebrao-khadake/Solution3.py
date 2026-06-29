#1
num = 10
unum = int(input("Give a number between 1 and 20: "))
if unum == num:
    print("correct")
else:
    print("wrong guess")

#2
num = 10
unum = int(input("Give a number between 1 and 20: "))
if unum == num:
    print("correct")
elif unum > num:
    print("high")
else:
    print("low")

#4
def guess_number():
    num = 10 

    while True:
        guess = int(input("Guess a number between 1 and 20: "))

        if guess == num:
            print("Right")
            break
        else:
            print("Wrong")

guess_number()
