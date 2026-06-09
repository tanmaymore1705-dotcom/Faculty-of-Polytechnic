#problem 1
num=10
while True:
    uinp= int (input("1,2,3,4,5,6,7,8,9,10="))
    if uinp !=num:
        print("incorrect")
    else:
        print("correct ")
#problem 2
n=5
student=[]
for x in range(n):
    name=input("Enter your name=")
    student.append(name)
    print(student)
