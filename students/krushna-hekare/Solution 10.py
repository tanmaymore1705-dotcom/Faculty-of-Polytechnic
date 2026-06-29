#problem 1
def classify_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F" 
print(classify_grade(95))
print(classify_grade(82))  
print(classify_grade(74))  
print(classify_grade(61))  
print(classify_grade(45))

#problem 2
def is_leap_year(year):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return True
    else:
        return False

print(2000, is_leap_year(2000))   
print(1900, is_leap_year(1900))   
print(2024, is_leap_year(2024)) 
print(2023, is_leap_year(2023))

#problem 3
def sum_to_n(n):
    total = 0  

    for i in range(1, n + 1):
        total += i

    return total

n = int(input("Enter a number: "))

print("Sum =", sum_to_n(n))

#problem 4

def times_table(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")
n = int(input("Enter a number: "))
times_table(n)
