def about_me():
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    city = input("Enter your city: ")
    fav_lang = input("Enter your favourite programming language: ")
    years = int(input("How many years have you been coding? "))

    bio = f"""
**About Me**
Name: {name}
Age: {age}
City: {city}
Favourite Language: {fav_lang}
Years Coding: {years}
"""
    
    print(bio)

about_me()
