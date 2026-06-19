def is_leap_year(year):
    if year%4==0 and year%100!=0:
        print("true")
    else:
        print("false")
year=int(input("enter a year:"))
is_leap_year(year)

