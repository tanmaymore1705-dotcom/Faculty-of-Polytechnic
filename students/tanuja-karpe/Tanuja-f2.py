#problem1
s={'a','b','c','d'}
s.update({'e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','y','z'})
print(s)
count=0
count=26
v={'a','e','i','o','u'}
for x in v:
         if x in s:
           count=count-1
print(count)

#problem2
s={'a','b','c','d'}
s.update({'e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','y','z'})
print(s)
count=0
v={'a','e','i','o','u'}
for x in v:
         if x in s:
           count=count+1
print(count)

#problem3
num=10
unum=int(input("guess a num bet 1 to 10="))
if(num>unum):
    print("low")
elif(num<unum):
    print("high")
else:
    print("correct guess")

#problem4
uinp=0
n=5
student=[]
for x in range(n):
    uinp=input("enter a student name=")
    student.append(uinp)
print(student)

#problem5
def greet():
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    print(f"Hi {name}! Next year you will be {age + 1}.")
greet()
