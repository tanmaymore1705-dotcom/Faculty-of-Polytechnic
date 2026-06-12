nos = 5
Students = []

for i in range(nos):
    name = input("Enter name: ")
    Students.append(name)

print(Students)
#solution5
def calculate(l, b, h):
    if (h>0):
        volume = l*b*h
        perimeter = 4 * (l+b+h)
        return ( volume , perimeter)
    
    else:
        area = l*b
        perimeter = 2 * (l+b)
        return ( area, perimeter)



print("Cuboid:", calculate(5, 3, 4))
print("Rectangle:", calculate(5, 3,0))
