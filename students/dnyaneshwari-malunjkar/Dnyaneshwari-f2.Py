#problem 1
s={'a','b','c','d'}
s.update({'e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','y','z'})
print(s)
count=0
count= 26
vowels ={'a','e','i', 'o', 'u'}

for x in s:
     if x in vowels:
        count = count - 1

print("Vowel count:", count)

#problem 2

letters = {'a', 'b', 'c', 'd', 'e', 'f', 'g',
           'h', 'i', 'j', 'k', 'l', 'm', 'n',
           'o', 'p', 'q', 'r', 's', 't', 'u',
           'v', 'w', 'x', 'y', 'z'}

vowels = set()
consonants = set()

for ch in letters:
    if ch in {'a', 'e', 'i', 'o', 'u'}:
        vowels.add(ch)
    else:
        consonants.add(ch)



print("Vowels Set =", vowels)
print("Consonants Set =", consonants) 

#problem

num = 10
guess = int(input("Guess a number 1 to 10: "))

if guess == num:
    print("Correct guess")
elif guess < num:
    print("Too low")
else:
    print("Too high")

#problem
n=5
student =[]
for i in range(n):
    name = input("enter student name:")
    student.append(name)
print (student)

