s = {'a','b','c','d','e','f','g','h','i','j','k','l',
     'm','n','o','p','q','r','s','t','u','v','w','x','y','z'}

c = 0

for x in s:
    if x not in ('a','e','i','o','u'):
        c += 1

print(c)

problem 
nos = 5
Students = []

for i in range(nos):
    name = input("Enter name: ")
    Students.append(name)

print(Students)
