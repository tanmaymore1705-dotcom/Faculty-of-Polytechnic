t=0
n=1
while n<=10:
  t+=n
  n+=1
print(t)
#problem2
a=4
b=9
c=19
def check(n):
     if(n%2=0):
        print("even")
     else:
        print("odd")

check(a)
check(b)
check(c)
#problem3
a=4
b=9
c=19
def check(n):
     if(n%3==0):
      print("divisible")
     else:
      print ("not divisible ")
check(a)
check(b)
check(c)
#problem 4
n=[1,2,3]
def check(n=list):
     for x in n:
         print (x)
         
check (n)
#problem5
l=[1,2,3,4,5,6]
l.pop(0)
l.pop(1)
l.pop(2)
print (l)
#problem6
l=[1,2,3,4,5,6]
l.pop(4)
l.pop(2)
l.pop(0)
print (l)
#problem7
d={"ram":30,"vijay":40,"Radha":50} 
print (d["vijay"])
#problem 7
d={"ram":30,"vijay":40,"Radha":50} 
d.update({"tom":2,"dom":10})
print(d) 
