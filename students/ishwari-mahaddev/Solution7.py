def is_leap_year(year):
    if (year % 4== 0):
      return True
    else:
        return False
year = int(input("Enter year: "))

print(year, "->", is_leap_year(year))
print(is_leap_year(2020))  
