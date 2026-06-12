t=0
n=1
while n<=10:
  t+=n
  n+=1
print(t)
#problem2
a=4
b==9
c=19
def even_odd(n)
  if n % 2 == 0:
    return "Even"
  else:
    return "odd"
    print(even_odd(a))
    print(even_odd(b))
    print(even_odd((c))
    #problem3
 a = 4
b = 9
c = 19

def divisible_by_3(e):
    if e % 3 == 0:
        return "Divisible by 3"
    else:
        return "Not divisible by 3"

print(divisible_by_3(a))
print(divisible_by_3(b))
print(divisible_by_3(c))

#problem4
 a = [1, 2, 3]

def print_elements(lst):
    for x in lst:
        print(x)

print_elements(a)
#problem 5
i = 1
L = [1, 2, 3, 4, 5, 6]
L.pop(0)
L.pop(1)
L.pop(2)
print(L)

# Problem 6
i = 0
L = [1, 2, 3, 4, 5, 6]
L.pop(4)
L.pop(2)
L.pop(0)
print(L)
# problem 7
d = {"Ram": 30, "Vijay": 40, "Radha": 60}

print(d["Vijay"])

d.update({"Tom": 2, "Don": 10})

print(d)





#problem7
num=10
unum=0
while unum != num:
    uinp=int(input(".....1-10:"))
    unum=uinp
    print("incorrect guess")
print("correct...")

#problem8
num = 10

guess = int(input("Guess a number between 1 and 100: "))

if guess == num:
    print("Correct Guess")
elif guess < num:
    print("Too Low")
else:
    print("Too High")

#problem9
num = 10

for unum in [5, 20, 10]:
    if unum == num:
        print(unum, "- Correct")
    elif unum < num:
        print(unum, "- Low")
    else:
        print(unum, "- High")
#problem10
def greet():
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))

    print("Hi", name + "!", "Next year you will be", age + 1)

greet()

#problem11

def tip_calculator():
    bill = float(input("Enter bill amount: "))
    tip_percent = float(input("Enter tip percentage: "))

    tip = bill * tip_percent / 100
    total = bill + tip

    print(f"Tip: {tip:.2f}")
    print(f"Total: {total:.2f}")

tip_calculator()



#Problem8
num=10
unum=0
while True :
    uinp=int(input("....."))
    unum=uinp
    if uinp !=num:
        print("incorrect")
    else:
        print("correct")
        break




#Problem9
n = 5
students = []

for i in range(n):
    name = input(f"Enter name of student {i+1}: ")
    students.append(name)

print("Student Names:")
