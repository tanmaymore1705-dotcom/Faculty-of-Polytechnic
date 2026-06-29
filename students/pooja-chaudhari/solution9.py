##problem 1
score=int(input("enter score="))
def classify_grade(score):
    if score>=90:
        print("A")
    elif score>=80 and score<90:
        print("B")
    elif score>=70 and score<80:
        print("C")
    elif score>=60 and score<70:
        print("D")
    else: 
        print("F")
classify_grade(score)
##problem 2
def is_leap_year(year):
    if year%4==0 and year%100!=0:
        print("True")
    else:
        print("False")
year=int(input("Enter a year="))
is_leap_year(year)
#problem 3
def sum_to_n(n):
    t=0
    for x in range(1,n+1):
        t=t+x
    return t
number=int(input("Enter a number="))
print(sum_to_n(number))
##problem 4
def times_table(n):
    for i in range(1,11):
        print(n*i)
times_table(7)
