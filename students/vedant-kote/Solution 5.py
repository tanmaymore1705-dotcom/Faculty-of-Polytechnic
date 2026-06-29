#problem no1
n=5
students=[]
for x in range(n):
    name=input (f"enter the name of student {x+1}:")
    students.append(name)
print("student")

#problem no2
def input_students(n):
    students = []

    for i in range(n):
        name = input(f"Enter the name of student {i + 1}: ")
        students.append(name)

    return students

student = input_students(50)
print(student)
