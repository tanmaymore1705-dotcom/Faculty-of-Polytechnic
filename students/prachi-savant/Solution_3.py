def countdown(n):
    while n >= 1:
        print(n)
        n -= 1
    print("Liftoff!")

def first_multiple(n, start):
    x = start
    while True:
        if x % n == 0:
            return x
        x += 1

countdown(5)
print(first_multiple(7, 50))   # 56
print(first_multiple(10, 10))  # 10
