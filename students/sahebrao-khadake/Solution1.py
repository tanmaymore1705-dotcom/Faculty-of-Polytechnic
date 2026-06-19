#program 1 vowels

s = {'a', 'b', 'c', 'd'}

s.update({'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
          'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
          'w', 'x', 'y', 'z'})
print(s)

#program 2

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

#program 3

s = {'a', 'b', 'c', 'd', 'e', 'f', 'g',
     'h', 'i', 'j', 'k', 'l', 'm', 'n',
     'o', 'p', 'q', 'r', 's', 't', 'u',
     'v', 'w', 'x', 'y', 'z'}

c = 0

for x in s:
    if x != 'a' and x != 'e' and x != 'i' and x != 'o' and x != 'u':
        c = c + 1

print("Number of consonants =", c)

#program 4

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
