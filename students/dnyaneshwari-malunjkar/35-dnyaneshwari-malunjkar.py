i=1
sum=0
while i<=10:
  sum= sum+i
  i=i+1
print(sum)
#problem 
a=4
b=9
c=19
def numbers(n):
    if n%2==0:
        print("even")
    else:
        print("odd")
numbers(a)
numbers(b)
numbers(c)
#problem 
a=4
b=9
c=19
def numbers (n):
    if n%3==0:
        print("divisible by 3")
    else:
        print("not divisible")
numbers(a)
numbers(b)
numbers(c)
#problem 
a=[1,2,3]
def print_list(list):
    for x in list:  # FIX(faculty): added the missing space ("inlist" -> "in list")
        print(x)
print_list(a)
#problem 
i=1
L=[1,2,3,4,5,6]
L.pop(0)
L.pop(1)
L.pop(2)
print(L)
#problem 
i=0
L=[1,2,3,4,5,6]
L.pop(4)
L.pop(2)
L.pop(0)
print(L)
#problem
d={"Ram":30,"Vijay":40,"Radha":60}  # FIX(faculty): dict needs quoted keys and ':' , e.g. {"Ram":30}
print(d["Vijay"])
#problem
d={"Ram":30,"Vijay":40,"Radha":60}  # FIX(faculty): was "(...}" with '=' -> use '{...}' with ':'
d.update({"Tom":2,"Don":10})  # FIX(faculty): update() takes a dict -> {"Tom":2}, not "Tom"=2
print(d) 
#problem 
s = {'a', 'b', 'c', 'd'}

s.update({'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
          'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
          'w', 'x', 'y', 'z'})

print(s)
#problem
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


 
