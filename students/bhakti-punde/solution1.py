letters={'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'}  # FIX(faculty): renamed from "set" so it doesn't shadow the built-in set() used below
count=0
for x in letters:
    if x not in ['a','e','i','o','u']:
        count=count+1
print (count)
#problem2
s={'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'}
vowels=set()
consonants=set()
for x in s:
    if x in ['a','e','i','o','u']:
        vowels.add(x)
    else:
        consonants.add(x)
print("vowels=",vowels)
print("consonants=",consonants)
