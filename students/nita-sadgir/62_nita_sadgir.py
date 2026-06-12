i=1
sum=0
while i<=10:
  sum= sum+i
  i=i+1
print(sum)
#problem 2
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
#problem 3
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
#problem 4
a=[1,2,3]
def print_list(list):
    for x in list:
        print(x)
print_list(a)