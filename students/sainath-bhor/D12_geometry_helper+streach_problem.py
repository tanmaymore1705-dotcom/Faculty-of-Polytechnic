def rectangle(width,height):
    area=width*height
    perimeter=2*(width+height)
    return area,perimeter
def circle(radius,pi=3.14159):
    area=pi*radius*radius
    circumference=2*pi*radius
    return area,circumference
def box(length,width,height):
    volume=length*width*height
    surface_area=2*(length*width+length*height+width*height)
    return volume,surface_area
def main():
    shape=input("Your shape is (rectangle/circle/cube) --> ")
    if shape== "rectangle":
        w=int(input("Enter width --> "))
        h=int(input("Enter height --> "))
        area, perimeter = rectangle(w, h)
        print("Area:", area)
        print("Perimeter:", perimeter)
    elif shape=="circle":
        r=int(input("Enter radius --> "))
        area,circumference = circle(r)
        print("Area:",area)
        print("Circumference:",circumference)
    elif shape=="cube":
        l= int(input("Enter length --> "))
        w= int(input("Enter width --> "))
        h= int(input("Enter height --> "))
        volume, surface_area = box(l, w, h)
        print("Volume:", volume)
        print("Surface Area:", surface_area)
    else:
        print("Invalid shape")
main()
