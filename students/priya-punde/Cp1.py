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
