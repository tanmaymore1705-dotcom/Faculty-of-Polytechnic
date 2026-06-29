#problem 1 - About Me
def ask_name():
    return input("Enter your name: ")

def ask_age():
    return int(input("How old are you? "))

def ask_city():
    return input("Which city are you from? ")

def ask_language():
    return input("Favourite programming language? ")

def ask_years():
    return int(input("How many years have you been coding? "))

def build_bio(name, age, city, language, years):
    divider = "=" * 40
    return (
        f"\n{divider}\n"
        f"            ABOUT ME\n"
        f"{divider}\n"
        f"Name:      {name}\n"
        f"Age:       {age}\n"
        f"City:      {city}\n"
        f"Codes in:  {language}\n"
        f"Coding for {years} years.\n"
        f"{divider}"
    )

def main():
    name = ask_name()
    age = ask_age()
    city = ask_city()
    language = ask_language()
    years = ask_years()
    print(build_bio(name, age, city, language, years))

main()

#problem 2 - D13 scope fix
def add_item(running_total, price):
    return running_total + price

def apply_tax(cart_total):
    return cart_total * 1.05

def run_cart():
    total = 0
    total = add_item(total, 40)
    total = add_item(total, 25)
    total = add_item(total, 15)
    print(f"Items added. Cart total: {total}")
    print(f"With 5% tax: {apply_tax(total):.2f}")

if __name__ == "__main__":
    run_cart()
