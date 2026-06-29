def classify_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80 and score < 90:
        return "B"
    elif score >= 70 and score < 80:
        return "C"
    elif score >= 60 and score < 70:
        return "D"
    else:
        return "F"

print(classify_grade(97))
print(classify_grade(83))
print(classify_grade(75))
print(classify_grade(64))
print(classify_grade(46))
