i=1
sum=0
while i<=10
  sum=sum+i
  i=i+1
print(sum)
#problem2
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
#problem3
a=4
b=9
c=19
def numbers(n):
    if n%3==0:
        print("divisible by 3")
    else:
        print("not divisible")
numbers(a)
numbers(b)
numbers(c)
#problem4
a=[1,2,3]
def print_list(list):
    for x in list:
        print(x)
print_list(a)
#problem
i=0
l=[1,2,3,4,5,6]
l.pop(4)
l.pop(2)
l pop(0)
print(l)
#problem6
i=0
l=[1,2,3,4,5,6]
l.pop(0)
l.pop(1)
l.pop(2)
print(l)
