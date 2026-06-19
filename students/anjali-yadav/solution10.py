#problem 1
def add_item(total, price):
    return total + price
def apply_tax(total):
    return total * 1.05
def main():
    total = 0
    total = add_item(total, 40)
    total = add_item(total, 25)
    total = add_item(total, 15)
    print("Cart total:", total)
    taxed_total = apply_tax(total)
    print("With tax:", taxed_total)
main()
#problem 2
def rectangle(width,height):
    area=width*height
    perimeter=2*(width+height)
    return area,perimeter
a,p=rectangle(3,4)
print(a)
print(p)
a,p=rectangle(10,2)
print(a)
print(p)
#problem 3
def circle(r,pi=3.14159):
    a=pi*r*r
    circumference=2*pi*r
    return a,circumference
a,c=circle(2)
print(round(a,2))
print(round(c,2))
a,c=circle(2,pi=3.14)
print(round(a,2))
print(round(c,2))
