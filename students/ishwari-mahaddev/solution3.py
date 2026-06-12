set={'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'}
vowel = []
consonants = []
for x in set:
    if x not in {'a','e','i','o','u'}:
         consonants.append(x)
    else:
        vowel.append(x)
print(vowel)
print(consonants)