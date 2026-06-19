def sum_to_n(n):
    t=0
    for x in range(1,n+1):
        t=t+x
    return t
number=int(input("Enter a number="))
print(sum_to_n(number))
