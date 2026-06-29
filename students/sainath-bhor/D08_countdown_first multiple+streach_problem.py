def countdown(n):
    while n > 0:
        print(n)
        n -= 1
    print("Liftoff!")

def first_multiple(n, start):
    x = start
    while True:
        if x % n == 0:
            return x
        x += 1

def count_steps(n):
    steps = 0
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        steps += 1
    return steps

countdown(5)
print(first_multiple(7, 50))  # 56
print(count_steps(6))
