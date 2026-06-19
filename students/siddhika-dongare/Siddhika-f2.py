#problem1
s = {'a', 'b', 'c', 'd'}

s.update({'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
          'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
          'w', 'x', 'y', 'z'})

print(s)
#problem2
s = {'a', 'b', 'c', 'd', 'e', 'f', 'g',
     'h', 'i', 'j', 'k', 'l', 'm', 'n',
     'o', 'p', 'q', 'r', 's', 't', 'u',
     'v', 'w', 'x', 'y', 'z'}

c = 0

for x in s:
    if x == 'a':
        c = c + 1
    elif x == 'e':
        c = c + 1
    elif x == 'i':
        c = c + 1
    elif x == 'o':
        c = c + 1
    elif x == 'u':
        c = c + 1
    else:
        continue

print("Number of vowels =", c)
#problem3
s = {'a', 'b', 'c', 'd', 'e', 'f', 'g',
     'h', 'i', 'j', 'k', 'l', 'm', 'n',
     'o', 'p', 'q', 'r', 's', 't', 'u',
     'v', 'w', 'x', 'y', 'z'}

c = 0

for x in s:
    if x != 'a' and x != 'e' and x != 'i' and x != 'o' and x != 'u':
        c = c + 1

print("Number of consonants =", c)
#problem4
S = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
     'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
     'u', 'v', 'w', 'x', 'y', 'z'}

V = set()
C = set()

for x in S:
    if x in "aeiou":
        V.add(x)
    else:
        C.add(x)

print("Vowels =", V)
print("Count of vowels =", len(V))


print("Consonants =", C)
print("Count of consonants =", len(C))

#problem4
num = 10

guess = int(input("Guess a number between 1 and 100: "))

if guess == num:
    print("Correct Guess")
elif guess < num:
    print("Too Low")
else:
    print("Too High")

#problem5
num = 10

for unum in [5, 20, 10]:
    if unum == num:
        print(unum, "- Correct")
    elif unum < num:
        print(unum, "- Low")
    else:
        print(unum, "- High")
#problem6 
def greet():
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))

    print("Hi", name + "!", "Next year you will be", age + 1)

greet()

#problem7

def tip_calculator():
    bill = float(input("Enter bill amount: "))
    tip_percent = float(input("Enter tip percentage: "))

    tip = bill * tip_percent / 100
    total = bill + tip

    print(f"Tip: {tip:.2f}")
    print(f"Total: {total:.2f}")

tip_calculator()
