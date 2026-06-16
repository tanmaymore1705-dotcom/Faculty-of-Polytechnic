#problem no 14
def about_me():
    name = input("What is your name? :-")
    age = int(input("How old are you? :-"))
    city = input("Which city are you from? :-")
    language = input("Favourite programming language? :-")
    years = int(input("How many years have you been coding? :-"))
    print("=" * 40)

    print("              ABOUT ME")

    print("=" * 40)
    
    print(f"Name:      {name}")
    print(f"Age:       {age}")
    print(f"City:      {city}")
    print(f"Codes in:  {language}")
    print(f"Coding for: {years} years.")
    
about_me()
