#problem 1
def greet():
    name=input("Enter your name:")
    age=int(input("Enter your age:"))
    print("Hi",name+"!Next year you will be", age+1)
greet()
#problem 2
num=10
unum=int(input("gives a num between 1 to 10: "))
if num<unum:
    print("high")
elif num>unum:
    print("low")
else:
    print("correct")
#problem 3
num=10
while True:
    uinp=int(input("1,2,3,4,5,6,7,8,9,10="))
    if uinp!=num:
        print("incorrect")
    else:
        print("correct")
#problem 4
n=5
student=[]
for x in range(n):
    name=input("Enter your name=")
    student.append(name)
    print(student)
