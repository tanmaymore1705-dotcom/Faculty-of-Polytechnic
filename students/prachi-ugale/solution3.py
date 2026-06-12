#problem 1
num = 10

unum = int(input("Guess a number between 1 and 10: "))

if unum < num:
    print("Low")
elif unum > num:
    print("High")
else:
    print("Correct")
