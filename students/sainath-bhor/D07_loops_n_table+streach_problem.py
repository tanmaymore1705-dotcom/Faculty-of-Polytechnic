#1
#using while loop
def sum_to_n():
    n=int(input("enter n to find count(count=1+2+..+n)-->"))
    count=0
    x=0
    while x<=n:
        count=count+x
        x=x+1 #sai
    print("count:",count)
sum_to_n()
#using for loop
def sum_to_n2():
    n=int(input("enter n to find count(count=1+2+..+n)-->"))
    sum=0 #sai
    for x in range(1,n+1):
        sum=sum+x
    print("sum :",sum)
sum_to_n2()

#2
def times_table():
    n=int(input("enter number whose table you want to see-->"))
    print(n,"×1 = ",n*1)#sai
    print(n,"×2 = ",n*2)
    print(n,"×3 = ",n*3)
    print(n,"×4 = ",n*4)
    print(n,"×5 = ",n*5)
    print(n,"×6 = ",n*6)
    print(n,"×7 = ",n*7)
    print(n,"×8 = ",n*8)
    print(n,"×9 = ",n*9)
    print(n,"×10 = ",n*10)
times_table()

#streach problem😉
def factorial():
    n=int(input("enter number to find factorial-->"))
    result=1
    x=1
    while x<=n:
        result=result*x
        x=x+1 #sai
    print("factorial of",n,"is:",result)
factorial()
