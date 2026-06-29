def ask_text(prompt):
    while True:
        text = input(prompt)
        if text:
            return text
        print("Can't be empty — try again.")


def ask_mark(prompt):
    while True:
        text = input(prompt)
        if not text.isdigit():
            print("Please enter a whole number.")
            continue
        mark = int(text)
        if 0 <= mark <= 100:
            return mark
        print("Mark must be between 0 and 100.")


def ask_yes_no(question):
    while True:
        answer = input(question).strip().lower()
        if answer == "y":
            return True
        if answer == "n":
            return False
        print('Please type "y" or "n".')


def collect_one_subject():
    name = ask_text("Subject name: ")
    m1 = ask_mark("  Mark 1 (0-100): ")
    m2 = ask_mark("  Mark 2 (0-100): ")
    m3 = ask_mark("  Mark 3 (0-100): ")
    return name, m1, m2, m3
    
