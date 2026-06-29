num=10
while True:
    uinp=int(input("Enter the number: "))
    if uinp!=num:
        print("incorrect guess")
    else:
        print("correct guess")
        break
#problem2
n=5
student=[]
for x in range(n):
    name=input("Enter your name: ")
    student.append(name)
print("student=")
print(student)
  
