def sum_to_n(n):
    t=0
    for x in range(1,n+1):
        t=t+x
    return t
number=int(input("Enter a number="))
print(sum_to_n(number))
#problem 2
score=int(input("Enter score: "))
def classify_grade(score):
    if score>=90:
        print('A')
    elif 89>=score and score>=80:
        print('B')
    elif 79>=score and score>=70:
        print('C')
    elif 69>=score and score >=60:
        print('D')
    else:
        print('F')
classify_grade(score)
#problem3
def is_leap_year(year):
    if year%4==0 and year%100!=0:
        print("True")
    else:
        print("False")
year=int(input("Enter a year="))
is_leap_year(year)
