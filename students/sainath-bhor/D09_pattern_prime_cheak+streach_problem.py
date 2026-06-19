def print_triangle(height):
    for row in range(1, height + 1):
        print('*' * row)

def is_prime(n):
    if n < 2:
        return False
    for d in range(2, n):
        if n % d == 0:
            return False
    return True

def primes_up_to(limit):
    for x in range(2, limit + 1):
        if is_prime(x):
            print(x)

print_triangle(5)
print(is_prime(7))   # True
print(is_prime(10))  # False
primes_up_to(20)
