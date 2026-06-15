def is_leap_year(year):
    if year%4==0 and year%100!=0:
        print("True")
    else:
        print("False")
year=int(input("Enter a year="))
is_leap_year(year)
