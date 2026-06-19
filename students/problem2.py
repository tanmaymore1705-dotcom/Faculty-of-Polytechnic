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
#problem 5
i=1
L=[1,2,3,4,5,6]
L.pop(0)
L.pop(1)
L.pop(2)
print(L)
#problem 6
i=0
L=[1,2,3,4,5,6]
L.pop(4)
L.pop(2)
L.pop(0)
print(L)
#problem 1
d={"ram":30,"vijay":40,"radha":60}
print(d["vijay"])
#problem 2
d={"ram":30,"vijay":40,"radha":60}
d.update({"tom":2,"don":10})
print(d)
#solution3
s = {'a','b','c','d','e','f','g','h','i','j','k','l',
     'm','n','o','p','q','r','s','t','u','v','w','x','y','z'}

c = 0

for x in s:
    if x not in ('a','e','i','o','u'):
        c += 1

print(c)solution3
nos = 5
Students = []

for i in range(nos):
    name = input("Enter name: ")
    Students.append(name)

print(Students)
x
