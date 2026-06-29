#problem2
s={'a','b','c','d','e','f','g',
   'h','i','j','k','l','m','n',
   'o','p','q','r','s','t','u','v'
   ,'w','x','y','z',}
count=0
for x in s:
    if x not in ['a','e','i','o','u']:  # FIX(faculty): was "for x not in[...]" -> invalid syntax; check each letter against the vowels
        count=count +1
print("no.of consonanta=", count)  # FIX(faculty): print the count variable (was "counts in", which is undefined)
