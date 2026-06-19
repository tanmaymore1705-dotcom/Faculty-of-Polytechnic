 # problem
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

#problem


def add_item(price, subtotal):
    return subtotal + price

def apply_tax(subtotal, tax_rate):
    tax = subtotal * tax_rate
    return subtotal + tax

def main():
    
    total = 0
    
    total = add_item(10, total)
    total = add_item(25, total)   
    total = add_item(5, total)    
    total = apply_tax(total, 0.10)  
    
    print(f"Correct total: {total}")

if __name__ == "__main__":
    main()
