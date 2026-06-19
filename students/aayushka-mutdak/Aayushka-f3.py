num = 10

unum = int(input("Guess a number between 1 to 20: "))

if unum < num:
    print("Low")
elif unum > num:
    print("High")
else:
    print("Correct")
#problem2
num=10
unum=0
while unum!=num:
    unum=int(input("guess a num bet 1 to 10="))
    if(unum==10):
        print("correct guess")
    else:
        print("incorrect guess")
        #problem 3
nos = 5
Students = []

for i in range(nos):
    name = input("Enter name: ")
    Students.append(name)

print(Students)
#problem3
def greet():
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    print(f"Hi {name}! Next year you will be {age + 1}.")
greet()



        
