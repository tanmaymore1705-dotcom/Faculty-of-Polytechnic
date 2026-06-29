def calculate(l, b, h):
    if h > 0:
        volume = l * b * h
        surface_area = 2 * (l*b + l*h + b*h)
        perimeter = 4 * (l + b + h)
        return volume, surface_area, perimeter
    else:
        return None

l = int(input("Enter length: "))
b = int(input("Enter breadth: "))
h = int(input("Enter height: "))
result = calculate(l, b, h)
if result:
    volume, surface_area, perimeter = result
    print(f"Volume: {volume}")
    print(f"Surface area: {surface_area}")
    print(f"Perimeter: {perimeter}")
