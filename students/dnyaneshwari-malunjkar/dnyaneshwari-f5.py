#problem 1
def countdown(n):
    while n > 0:
        print(n)
        n = n-1
    print("Liftoff!")

countdown(5)
# problm 2
def print_triangle(height):
    for row in range(1, height + 1):
        print('*' * row)

# Example
print_triangle(5)
