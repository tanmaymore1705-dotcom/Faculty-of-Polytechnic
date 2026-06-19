
#Problem1
l = [12, 19, 18, 36, 42]

for i in l:
    if i % 6 == 0:
        print( "multiple of 6")
    else:
        if(i % 6) % 2==0:
            print( "not a multiple of 6")
        else:
            print("not multiple")

#Problem2
l = [12, 19, 18, 36, 42]

for i in l:
    if i % 6 != 0:
        print( "rem is m of z")
    else:
        print("only multiple of 6")

#Problem3
m = int(input("No. of members: "))

names = []
ages = []

for i in range(m):
    name = input("Enter name: ")
    age = int(input("Enter age: "))

    names.append(name)
    ages.append(age)

print("Names:", names)
print("Ages:", ages)

#problem4
def area(l, b):
    return l * b

print(area(10, 5))
