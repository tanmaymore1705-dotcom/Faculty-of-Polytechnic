#program 1
d={}
m=int(input("no of members:"))
members={}
for x in range(m):
    name=input("enter members name:")
    age=int(input("enter members age:")) 
    d.update({name : age})
print(d)  # FIX(faculty): dedented out of the loop so the dict prints once at the end, not every iteration

#program 2

def area(l,b):
    a=l*b
    return(a)
l=float(input("length:"))
b=float(input("breath:"))
results=area(l,b)
print(results)
