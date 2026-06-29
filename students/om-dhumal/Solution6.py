#problem 1
def countdown(n):
    while n > 0:
        print(n)
        n -= 1
    print("Liftoff!")

n = int(input("Enter how many sceonds till lift off: "))
countdown(n)


#problem 2
def print_triangle(height):

    for row in range(1, height + 1):
        
        for star in range(row):
            print("*", end="")
        print()
print_triangle(5)
