N = 5
students = []

for i in range(N):
    name = input("Enter student name: ")
    students.append(name)

print("Student List:", students)


#Solution6.py
def rectangle(l, b):
    a = l * b
    return a

l = float(input("length: "))
b = float(input("breadth: "))

res = rectangle(l, b)
print(res)
