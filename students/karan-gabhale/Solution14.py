def sum_to_n(n):
    total = 0  

    for i in range(1, n + 1):
        total =total+ i

    print(total)
n=int(input("Enter number:"))
sum_to_n(n)
