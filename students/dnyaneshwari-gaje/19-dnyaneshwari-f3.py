# Module 1 - Basic loops and conditions

# Problem 1: Print numbers 1-10 with even/odd label
for i in range(1, 11):
    if i % 2 == 0:
        print(f"{i} - even")
    else:
        print(f"{i} - odd")

# Problem 2: Sum of 1 to N
def sum_to_n(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

print(sum_to_n(10))  # 55
