#problem
def countdown(n):
    while n > 0:
        print(n)
        n = n-1
    print("Liftoff!")

countdown(5)

 #problem 
def print_triangle(height):
    for row in range(1, height + 1):
        print('*' * row)

# Example
print_triangle(5)
