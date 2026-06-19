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
