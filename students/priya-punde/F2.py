#problem 1
s={'a','b','c','d'}
s.update({'e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','y','z'})
print(s)
count= 26
vowels ={'a','e','i', 'o', 'u'}

for x in s:
     if x in vowels:
        count = count - 1

print("consonets count:", count)
#problem2
s={'a','b','c','d'}
s.update({'e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','y','z'})
print(s)
count= 0
vowels ={'a','e','i', 'o', 'u'}

for x in s:
     if x in vowels:
        count = count +1
print ("vowels count:",count)
#problem2
s = {'a','b','c','d'}
s.update({'e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','y','z'})

vowels = {'a','e','i','o','u'}

v = {x for x in s if x in vowels}
c = {x for x in s if x not in vowels}

print("Vowels:", v)
print("Consonants:", c)
        



