#problem no1
def greet():
    name = input("Your name? ")
    age = int(input("Your age? "))

    print(f"Hi {name}! Next year you will be {age + 1}")
   
greet()

#problem no2
def tip_calculator():
    bill = float(input("Bill amount? "))
    tip_percent = float(input("Tip percentage? "))

    tip = bill * tip_percent / 100
    total = bill + tip

    print(f"Tip: {tip:.2f}")
    print(f"Total: {total:.2f}")

tip_calculator()
