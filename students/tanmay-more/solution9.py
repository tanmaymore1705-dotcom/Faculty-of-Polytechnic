def cub_rec(l, b, h):
    if h == 0:
        s = "rectangle"
        a = l * b
        p = 2 * (l + b)  
        return (s, a, p)
    else:
        s = "cuboid"
        v = l * b * h
        p = 8 * (l + b + h)  
        return (s, v, p)


l=int(input("enter length:")) 
b=int(input("enter breadth:"))
h=int(input("enter height:"))  

result = cub_rec(l, b, h)

print("Result is:", result)
