#problem 1

x = "name_surname_age"

info = x.split("_")

print(info)

#problem 2

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
