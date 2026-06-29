s={'a','b','c','d','e','f','g','h','i','j','k','l','n','o','p','q','r','s','t','u','v','w','x','y','z'}
count=0
for x in s:
    if x not in ['a','e','i','o','u']:
      count=count+1
print(count)
#problem2
s={'a','b','c','d','e','f','g','h','i','j','k','l','n','o','p','q','r','s','t','u','v','w','x','y','z'}
vowels=set()
consonents=set()
for x in s:
    if x  in['a','e','i','o','u']:
        vowels.add(x)
    else:
        consonents.add(x)
print("vowels=",vowels)
print("consonents=",consonents)
