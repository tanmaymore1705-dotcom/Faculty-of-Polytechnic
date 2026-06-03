x=0
while x<10:
  x=x+1
print(x)
#Problam2
a=2
b=26
c=37
l=[a,b,c]
for x in l:
  if x % 2==0:
    print(f"even")
  else:
    print(f"odd")
  #problem3
a=4
b=9
c=19
M=[a,b,c]
for x in M:
    if x % 3 ==0:
        print("divis")
    else:
        print("divisable")
    
      #problem4
q=[1,2,3]
def number(q):
  for x in q:
    print(x)
number(q)
#problem5
l=[1,2,3,4,5,6]
l.pop(4)
l.pop(2)
l.pop(0)
print(l)
