#problem no 2
n=5
students=[]
for x in range(n):
    name=input (f"enter the name of student {x+1}:")
    students.append(name)
print("students",students)

#problem no 3
def input_students(n):
    students = []

    for i in range(n):
        name = input(f"Enter the name of student {i + 1}: ")
        students.append(name)

    return students

student = input_students(50)
print(student)

#problem no 4
m = int(input("No of members: "))

d = {}

for x in range(m):
    name = input(f"Enter the name of student {x+1}: ")
    age = int(input("Enter age: "))
    
    d[name] = age

print("Student Details:")
print(d)
