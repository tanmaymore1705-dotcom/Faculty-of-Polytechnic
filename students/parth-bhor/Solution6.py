#1
n=5
students=[]
for x in range(n):
    name=input (f"enter the name of student {x+1}:")
    students.append(name)
print("student")



#2
def input_students(n):
    students = []

    for i in range(n):
        name = input(f"Enter the name of student {i + 1}: ")
        students.append(name)

    return students

student = input_students(50)
print(student)


#3
num = 10 
while True:
    guess = int(input("Guess a number between 1 and 20: "))
    if guess == num:
        print("Right")
        break  # FIX(faculty): added break so the loop stops on a correct guess (was an infinite loop)
    else:
        print("Wrong")


#4
num = 10 
while True:
    guess = int(input("Guess a number between 1 and 20: "))
    if guess == num:  # FIX(faculty): indented this if/else into the while loop (was outside it -> infinite loop with unreachable checks)
        print("Right")
        break
    else:
        print("Wrong")
