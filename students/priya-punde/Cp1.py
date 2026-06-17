#problem1
def avg(a,b,c):
    a=(a,b,c)/3
    return(a)
#problem2
def l_g(avg):
    if avg>=90:
        return"A"
    elif avg>=80:
        return"B"
    elif avg>70:
        return"C"
    elif avg>=60:
        return"D"
    else:
        return"F"
print(l_g(35))
#problem3
def fo_ma(m1,m2,m3):
    return(f"{m1},{m2},{m3}")
print(fo_ma(20,4,5))
#problem4

def classify_result(avg):
    if avg>=75:
        print("disc")
    elif avg>=35:
        print("pass")
    else:
        print("fail")
classify_result(56)
