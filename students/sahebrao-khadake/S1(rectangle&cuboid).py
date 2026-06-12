#1
def area(l, b, h):
    if h == 0:
        print("shape is rectangle")
        print("Area of rectangle is:", l * b)
        print("Perimeter of rectangle is:", 2 * (l + b))
    else:
        print("shape is cuboid")
        print("Volume of cuboid is:", l * b * h)
        print("Perimeter of cuboid is:", 8 * (l + b + h))

l = int(input("Enter length: "))
b = int(input("Enter breadth: "))
h = int(input("Enter height (if rectangle type 0): "))

area(l, b, h)
