# problem 1
n=int(input("enter your number="))
def countdown(n):
    while n>=1:
        print(n)
        n=n-1
    print("Liftoff")
countdown(n)
#problem 2
def print_triangle(height):
    row=1
    while row<=height:
        print("*"*row)
        row=row+1
print_triangle(10)
