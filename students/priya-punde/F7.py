def classify_grade(score):
    if(score>=90):
        print("A")
    elif(score>=80 and score<90):
         print("B")
    elif(score>=70 and score<=80):
         print("C")
    elif(score>=60 and score<70):
         print("D")
    else:
          print("E")
score=int(input("enter a num:")) 
classify_grade(score)
# problem leap year
def leap_year(y):
    if(y%4==0 and y%100!=0):
        print("True")
    else:
        print("false")
year=int(input("enter a year:"))
leap_year(year)
#problem sum
def sum(n):
    total=0
    for x in range(1,1+n):
        total+=x
    return total

print(sum(10))
#problem table 
def table(n):
    for i in range(1, 11): 
        print(n*i)
table(7)
