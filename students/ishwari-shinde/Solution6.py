#problem 
#information
name = input("Name: ")
age = int(input("Age: "))
city = input("City: ")
lang = input("Favourite language: ")
years = int(input("Coding years: "))

print(f"Name: {name}\nAge: {age}\nCity: {city}\nLanguage: {lang}\nCoding Years: {years}")

#problem 2
#whole numbers 
while True:
    name = input("Name: ")
    if name:
        break
    print("Name can't be empty — try again.")

while True:
    age = input("Age: ")
    if age.isdigit():
        age = int(age)
        break
    print("Please type a whole number.")

print(name, age)
