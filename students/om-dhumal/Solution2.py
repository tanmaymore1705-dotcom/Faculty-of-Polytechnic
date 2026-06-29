# problem 1
num=19
guess=int(input("Guess the number:"))
while guess != num:
  print("Wrong Guess. Try again")
  guess=int(input("Guess the number:"))

if guess == num:
  print("You guessed correctly good job")

#problem1

num=67
unum=int(input("Enter your number:"))
if unum<num:
    print("Too Low")
elif unum>num:
    print("Too High")
else:
    print("correct guess good job ")  
