#problem 1
#times_table
def times_table(n):
    for i in range(1, 11):
        print(n, "x", i, "=", n * i)

times_table(7)

#problem 2
#total range
def sum(n):
    total=0
    for x in range(1,n+1):
        total+=x
    print(total)
sum(10)


