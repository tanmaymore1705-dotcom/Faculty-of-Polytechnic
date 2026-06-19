num=10
unum=int(input("guess a num bet 1 to 10="))
if(unum<num):   # FIX(faculty): compare the user's guess (unum) to num, not the constant num to 10
    print("low")
elif(unum>num):  # FIX(faculty): same here -> was always false, so it only ever printed "correct guess"
    print("high")
else:
    print("correct guess")

#problem2
def rectangle(l,b):

    a=l*b
    
    return(a)
l=int(input("enter length:"))
b=int(input ("enter breadth:"))
result=rectangle(l,b)
print (result )
