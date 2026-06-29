#problem 1
# consonants 
s = {'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'}
count =0
for x in s:
    if x not in['a','e','i','o','u']:
        count=count+1
print("no. of consonants=",count)
