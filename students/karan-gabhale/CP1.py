#problem 1
def avrage_of_three(m1,m2,m3):
    return round(m1,m2,m3)/3
 
#problem 2
def classify_result(a):
    if a>=75:
        return("distinction")
    elif a>=35:
        return("pass")
    else:
        return("fall")  

#problem 3      
  
def classify_result(a):
    if a>=90:
        return("A")
    elif a>=80:
        return("B")
    elif a>=70:
        return("C")
    elif a>=60:
        return("d")
    elif a<60:
        return("F")

#problem 4
def  format_marks(m1, m2, m3):
     return(f"{m1},{ m2},{ m3}")


