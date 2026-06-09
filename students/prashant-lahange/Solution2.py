x=0
total=0
while x<10:
 X=X+1
 total=total+1
 print(total)

#problem 2

def even_odd(number):
if number%2==0:
   return "even"
else:
   return "odd"
a-4
b-9
c-19
print("a", even_odd(a))
print("b",even_odd(b))
print("c",even_odd(c))
#problem 3

def div_3(num):
if num %3==0:
    return("divisible by 3")
else:
    return("not divisible by 3")
a=4
b=9
c=19
print("a", div_3(a))
print("b", div_3(b))
print("c", div_3(c))



#problem 4
a=[1,2,3]
def print_ele(a):
  i=0
  for x in a:
    i=i+1
    print(1)
    
print_ele(a)

# problem 5
1=[1,2,3,4,5,6]
1.pop(0)
print(1)
1.pop(1)
print(1)
1.pop(2)
print(1)

# problem 6
1=[1,2,3,4,5,6]
1.pop(4)
print(1)
1.pop(2)
print(1)
1.pop(0)
print(1)

# problem 7
d={"Ram":30,"Vijay":40,"Radha":60}
print(d["Vijay"])
d.update({"Tom":2,"Don":10})
print(d)
