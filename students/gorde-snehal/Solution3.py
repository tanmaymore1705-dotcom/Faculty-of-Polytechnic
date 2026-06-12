num = 10

unum = int(input("Guess a number: "))

if unum == num:
    print("Correct guess")
elif unum > num:
    print("High")
else:
    print("Low")
