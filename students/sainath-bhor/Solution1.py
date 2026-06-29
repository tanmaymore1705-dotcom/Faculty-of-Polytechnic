#problem 1
x=0
total=0
while x<10:
    x=x+1
  total=total+x
print(total)

#problem 2
def even_odd(number):
  if number % 2==0:
    return "Even"
  else:
    return"odd"
a=2
b=26
c=37
print("a",even_odd(a))
print("b",even_odd(b))
print("c",even_odd(c))

#Problem 3
def div_3(number):
  if number % 3==0:
    return ("divisible by 3")
  else:
    return ("non divisible by 3")

a=4
b=9
c=19
print("a=",div_3(a))
print("b=",div_3(b))
print("c=",div_3(c))

#problem 4
a=[1,2,3]
def print_list(list):
 for x in list:
     print(x)
print_list(a)
