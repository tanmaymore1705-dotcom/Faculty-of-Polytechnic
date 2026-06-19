x=0
while x<10:
  x=x+1
print(x)
#Problam2
a=2
b=26
c=37
l=[a,b,c]
for x in l:
  if x % 2==0:
    print(f"even")
  else:
    print(f"odd")
  #problem3
a=4
b=9
c=19
M=[a,b,c]
for x in M:
    if x % 3 ==0:
        print("divis")
    else:
        print("divisable")
    
      #problem4
q=[1,2,3]
def number(q):
  for x in q:
    print(x)
number(q)
 #problem5
l=[1,2,3,4,5,6]
l.pop(4)
l.pop(2)
l.pop(0)
print(l)
 #problem 6
d={"Ram": 30,"Vijay": 40,"Radha": 60}
print(d["Vijay"])
 #problem 7
d={"Ram": 30,"Vijay": 40,"Radha": 60}
d.update({"tom" : 10})
d.update({"don": 2})
print(d)
#problem 8
s = {'a', 'b', 'c', 'd'}

s.update({'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
          'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
          'w', 'x', 'y', 'z'})

print(s)
 #problem 9
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
 #problem 10
s = {'a', 'b', 'c', 'd', 'e', 'f', 'g',
     'h', 'i', 'j', 'k', 'l', 'm', 'n',
     'o', 'p', 'q', 'r', 's', 't', 'u',
     'v', 'w', 'x', 'y', 'z'}

c = 0

for x in s:
    if x != 'a' and x != 'e' and x != 'i' and x != 'o' and x != 'u':
        c = c + 1

print("Number of consonants =", c)

 #problem11
letters = {'a', 'b', 'c', 'd', 'e', 'f', 'g',
           'h', 'i', 'j', 'k', 'l', 'm', 'n',
           'o', 'p', 'q', 'r', 's', 't', 'u',
           'v', 'w', 'x', 'y', 'z'}

vowels = set()
consonants = set()

for s in letters:
    if s in {'a', 'e', 'i', 'o', 'u'}:
        vowels.add(s)
    else:
        consonants.add(s)

print("Vowels Set =", vowels)
print("Consonants Set =", consonants)


#problem 12
num = 10

unum = int(input("Guess a number between 1 to 20: "))

if unum < num:
    print("Low")
elif unum > num:
    print("High")
else:
    print("Correct")

 
