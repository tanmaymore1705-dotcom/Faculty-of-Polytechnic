#problem no 1
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

score = int(input("Enter score (0-100): "))
grade = classify_grade(score)

print("Grade  =", grade)

#problem no 2
def is_leap_year(year):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return True
    else:
        return False

print(2000, is_leap_year(2000))   
print(1900, is_leap_year(1900))   
print(2024, is_leap_year(2024)) 
print(2023, is_leap_year(2023))
