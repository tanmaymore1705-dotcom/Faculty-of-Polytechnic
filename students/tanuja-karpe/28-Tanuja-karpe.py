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
def check_even(n):
     if(n%2==0):
        print("even")
     else:
        print("odd")

check_even(a)
check_even(b)
check_even(c)
#problem3
a=4
b=9
c=19
def check_div3(n):
     if(n%3==0):
      print("divisible")
     else:
      print ("not divisible ")
check_div3(a)
check_div3(b)
check_div3(c)
#problem 4
n=[1,2,3]
def check_list(n):
     for x in n:
         print (x)

check_list(n)
#problem5
l=[1,2,3,4,5,6]
l.pop(0)
l.pop(1)
l.pop(2)
print (l)
