# problem 

d={}
m=int(input("no of members:"))
members={}
for x in range(m):
    name=input("enter members name:")
    age=int(input("enter members age:")) 
    d.update({name : age})
    print (d)
  
# problem 

def area(l,b):
    a=l*b
    return(a)
l=float(input("length:"))
b=float(input("breath:"))
results=area(l,b)
print(results)

   #problem 

x = "name_surname_age"

info = x.split("_")

print(info)

#problem 

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

