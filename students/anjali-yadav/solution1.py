#problem 1
s= ({'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'})
count=0
for x in s:
    if x not in['a','e','i','o','u']:
        count=count+1
print("no.of consonants=",count)
#problem 2
s= ({'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'})
vowels=set()
consonants=set()
for x in s:
    if x in['a','e','i','o','u']:
        vowels.add(x)
    else:
        consonants.add(x)
print("vowels=",vowels)
print("consonants=", consonants)
