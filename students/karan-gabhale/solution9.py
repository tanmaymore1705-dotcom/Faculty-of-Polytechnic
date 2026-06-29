#problem 1

def cub_res(l, b, h):
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

l = int(input("Enter length: "))
b = int(input("Enter breadth: "))
h = int(input("Enter height: "))

result = cub_res(l, b, h)
print(result)
