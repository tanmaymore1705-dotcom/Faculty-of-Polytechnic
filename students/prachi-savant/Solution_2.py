def area(l, b):
    return l * b

print(area(5, 4))
#problem 2
def classify_grade(score):
    if score >= 90:
        print AA"
    elif score >= 80:
       print "B"
    elif score >= 70:
       print "C"
    elif score >= 60:
       print "D"
    else:
       print "F"
        score = int(input("enter your score"))
        class_g(score)

#problem 3
def is_leap_year(year):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        print(True)
    else:
        print(False)

year= int(input("enter a year:"))
is_leap_year(year)


#problem 4
def sum_to_n(n):
    total = 0  # running total

    for i in range(1, n + 1):
        total += i

    return total 
    
print(sum_to_n(5))   # 15
print(sum_to_n(1))   # 1
print(sum_to_n(10))  # 55

#problem 5
def table(n)
for i in range(1,11):
    print(n*i)
    table(7)

    
