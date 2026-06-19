def ask_text(p): return input(p)
def ask_int(p): return int(input(p))

def build_bio(n,a,c,l,y):
    return f"Name: {n}\nAge: {a}\nCity: {c}\nCodes in: {l}\nCoding for {y} years."

def main():
    print(build_bio(
        ask_text("Name: "),
        ask_int("Age: "),
        ask_text("City: "),
        ask_text("Language: "),
        ask_int("Years: ")
    ))

main()
