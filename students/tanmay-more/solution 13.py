3problem no 1
def countdown(n):
    while n > 0:
        print(n)
        n -= 1
    print("Liftoff!")

n = int(input("Enter how many sceonds till lift off: "))
countdown(n)

#problem no 1
def print_triangle(height):
     for row in range(1, height + 1):
        for star in range(row):
            print("*", end=" ")
        print()
height=int(input("enter height:"))
print_triangle(height)
