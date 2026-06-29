# problem 1 - sum 1 to 10
x = 0
total = 0
while x < 10:
    x = x + 1
    total = total + x
print(total)

# problem 2
def even_odd(number):
    if number % 2 == 0:
        return "even"
    else:
        return "odd"

a = 4
b = 9
c = 19
print("a", even_odd(a))
print("b", even_odd(b))
print("c", even_odd(c))

# problem 3
def div_3(num):
    if num % 3 == 0:
        return "divisible by 3"
    else:
        return "not divisible by 3"

a = 4
b = 9
c = 19
print("a", div_3(a))
print("b", div_3(b))
print("c", div_3(c))

# problem 4
a = [1, 2, 3]
def print_ele(lst):
    for x in lst:
        print(x)

print_ele(a)

# problem 5
lst = [1, 2, 3, 4, 5, 6]
lst.pop(0)
print(lst)
lst.pop(1)
print(lst)
lst.pop(2)
print(lst)

# problem 6
lst = [1, 2, 3, 4, 5, 6]
lst.pop(4)
print(lst)
lst.pop(2)
print(lst)
lst.pop(0)
print(lst)

# problem 7
d = {"Ram": 30, "Vijay": 40, "Radha": 60}
print(d["Vijay"])
d.update({"Tom": 2, "Don": 10})
print(d)
