#problem 1
x=0
total=0   # FIX(faculty): initialise total before the loop (was used before assignment -> NameError)
while x<10:
  x=x+1
  total=total+1
  print(total)

#problem 2
def even_odd(number):
    if number % 2 == 0:
        return "even"
    else:
        return "odd"
a=4
b=9
c=19

print("a",even_odd(a))
print("b",even_odd(b))
print("c",even_odd(c))

# problem 3

def div_3(number):
    if number % 3 ==0:
        return("divisible by 3")
    else:
        return("not divisible by 3")
a=4
b=9
c=19

print("a",div_3(a))
print("b",div_3(b))
print("c",div_3(c))

#problem 4
def print_elements(lst):
    for item in lst:
        print(item)

d = [1, 2, 3]
print_elements(d)

#problem 5

l=[1,2,3,4,5,6]

l.pop(0)
l.pop(1)
l.pop(3)

print(l)

#problem 6
l=[1,2,3,4,5,6]

l.pop(4)
l.pop(2)
l.pop(0)

print(l)
