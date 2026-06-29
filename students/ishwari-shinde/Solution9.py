#problem 1
#add item

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
    print("With tax:", apply_tax(total))


main()

#problem 2
#information 
def name():
    n=input ("enter name:")
    return (n)
    def age():
        a=input ("enter age:")
        return (a)
        def city ():
            c=input ("enter city:")
            return(c)
            def main():
                N=name()
                A=agr()
                C=city ()
                print(f"{N}, {A}, {C}")
                


#problem 3
#rectangle
def rectangle(width, height):
    area = width * height
    perimeter = 2 * (width + height)
    return area, perimeter

a, p = rectangle(3, 4)
print(a)   
print(p)  


#problem 4
#circle

def circle(r)
 a=π*(r**2) pi=3.14
 return (a)
