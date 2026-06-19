#problem 1 - D13 scope fix
def add_item(running_total, price):
    return running_total + price

def apply_tax(cart_total):
    return cart_total * 1.05

def main():
    total = 0
    total = add_item(total, 40)
    total = add_item(total, 25)
    total = add_item(total, 15)
    print(f"Items added. Cart total: {total}")
    print(f"With 5% tax: {apply_tax(total):.2f}")

if __name__ == "__main__":
    main()

#problem 2 - About Me
def ask_name():
    return input("Enter your name: ")

def ask_age():
    return int(input("Enter your age: "))

def ask_city():
    return input("Enter your city: ")

def ask_lang():
    return input("Enter your favourite programming language: ")

def ask_years():
    return int(input("How many years have you been coding? "))

def show_bio(name, age, city, lang, years):
    print("=" * 40)
    print("            ABOUT ME")
    print("=" * 40)
    print(f"Name:      {name}")
    print(f"Age:       {age}")
    print(f"City:      {city}")
    print(f"Codes in:  {lang}")
    print(f"Coding for {years} years.")
    print("=" * 40)

def about_me():
    name = ask_name()
    age = ask_age()
    city = ask_city()
    lang = ask_lang()
    years = ask_years()
    show_bio(name, age, city, lang, years)

about_me()

#problem 3 - Geometry
def rectangle(l, b):
    return l * b

def circle(r, pi=3.14159):
    return pi * r * r

print(rectangle(2, 3))
print(round(circle(3), 2))

#problem 4 - Student report card
for x in range(3):
    n = input("Enter name: ")
    a = int(input("Enter marks: "))
    b = int(input("Enter marks: "))
    c = int(input("Enter marks: "))
    t = a + b + c
    av = t / 3
    print("Name: " + n)
    print("Total: " + str(t) + " / 300")
    print("Average: " + str(round(av, 2)))
    if av < 35:
        print("Result: FAIL")
    elif av >= 75:
        print("Result: PASS (Distinction)")
    else:
        print("Result: PASS")
    print("-----------------------")
