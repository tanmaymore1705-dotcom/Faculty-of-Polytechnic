#problem 1
def cub_rec(l,b,h):
    if h==0:
        s="rectangle"
        a=l*b
        p=2*(l+b)
        return(s, a, p)
    else:
        s="cuboid"
        v=l*b*h
        p=8*(l+b+h)
        return(s,v,p)
a,b,c=cub_rec(2,3,4)
print("Shape=",a)
print("Volume=",b)
print("Perimeter=",c)
#problem 2
info= input("Enter your name,surname,age=").split()
print(info)
