#problem1
def about_me():
    name = str(input("Enter your name: "))
    age = int(input("Enter your age: "))
    city = str(input("Enter your city: "))
    fav_programming_lang = str(input("Enter your favourite programming language: "))
    code_yr = int(input("How many years you have been coding? "))

    print("=== About Me ===")
    print("Name =", name)
    print("Age =", age)
    print("City =", city)
    print("Language =", fav_programming_lang)
    print("Coding Years =", code_yr)

about_me()
