#1 grade classification 
def classify_grade():
    score=int(input("Number of marks: "))
    if score>=90:
        return "A"
    elif score>=80:
        return "B"
    elif score>=70:
        return "C"
    elif score>=60:
        return "D"
    else:
        return "F"
#sai
classify_grade()
grade = classify_grade()
print("Grade:", grade)

#2 leapyear cheacker
year=int(input("enter year you want to cheak leap or not"))
if year%4==0 and (year%100!=0 or year%400==0):
    print(f"{year} is leap year")
else: #sai
    print(f"{year} is not leap")
