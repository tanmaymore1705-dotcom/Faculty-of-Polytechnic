#problem 1

num=10
unum=int(input("Guess a num but 1 to 10:"))
if unum < num:
    print("to low")
elif unum > num:
      print("to high")
        
else:
    print("correct  Guess")
