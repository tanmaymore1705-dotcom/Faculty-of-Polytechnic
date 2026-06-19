#problem1
s={'a','b','c','d','e','f','g','h','i','j','k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'}
count=0
for x in s:
  if x=='a':
    count=count+1
  elif x=='e':
    count=count+1
  elif x=='i':
    count=count+1
  elif x=='o':
    count=count+1  
  elif x=='u':
    count=count+1
  else:
    "continued"
print(count)

#problem2 
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
