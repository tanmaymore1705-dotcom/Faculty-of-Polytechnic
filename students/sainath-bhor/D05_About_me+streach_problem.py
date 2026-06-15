while True:
    name=input("What is your name?-->")
    if name!="":
        break
    else:
        print("name cant be empty")
age=int(input("How old are you? --> "))
city=input("Which city are you from? --> ")
language=input("Which one your favourite programing language? --> ")
years=int(input("How many years have you been coding? --> "))
print()  #sai
print("========================================")
print("            ABOUT ME")
print("========================================")
print(f"Name:      {name}")
print(f"Age:       {age}")
print(f"City:      {city}")
print(f"Codes in:  {language}")
print(f"Coding for {years} years")
print("========================================")
