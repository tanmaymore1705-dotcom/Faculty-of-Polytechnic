# Grade Buddy — CP4: Main Menu + History
#
# Read the full brief in problem.md.
# Add print_menu(), print_history(), and run() to your grade_buddy.py.
# Then change the bottom of the file to call run() instead of main().
#
# All prior functions are given below so you can run this file standalone.


# ── From CP1 (provided — do not modify) ──────────────────────────────────────

PASS_MARK = 35
DISTINCTION_MARK = 75


def average_of_three(m1, m2, m3):
    return round((m1 + m2 + m3) / 3, 1)


def classify_result(average):
    if average < PASS_MARK:
        return "FAIL"
    elif average >= DISTINCTION_MARK:
        return "DISTINCTION"
    return "PASS"


def letter_grade(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    return "F"


def format_marks(m1, m2, m3):
    return f"{m1}, {m2}, {m3}"


# ── From CP2 (provided — do not modify) ──────────────────────────────────────

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


# ── From CP3 (provided — do not modify) ──────────────────────────────────────

MAX_SUBJECTS = 5


def collect_all_subjects():
    subjects = []
    subjects.append(collect_one_subject())
    while len(subjects) < MAX_SUBJECTS:
        if not ask_yes_no("Add another subject? (y/n): "):
            break
        subjects.append(collect_one_subject())
    if len(subjects) == MAX_SUBJECTS:
        print("Maximum 5 subjects reached.")
    return subjects


def build_subject_row(name, m1, m2, m3):
    avg = average_of_three(m1, m2, m3)
    grade = letter_grade(avg)
    result = classify_result(avg)
    return f"{name:<16}| {m1:>3} | {m2:>3} | {m3:>3} | {avg:<4} | {grade:^5} | {result}"


def print_report(subjects):
    border = "=" * 60
    divider = "-" * 60
    print(border)
    print(f"{'GRADE REPORT':^60}")
    print(border)
    print(f"{'Subject':<16}| M1  | M2  | M3  | Avg  | Grade | Result")
    print(divider)
    total = 0
    for name, m1, m2, m3 in subjects:
        print(build_subject_row(name, m1, m2, m3))
        total += average_of_three(m1, m2, m3)
    print(divider)
    print(f"Overall Average: {round(total / len(subjects), 1)}")
    print(border)


# ── CP4: Your three new functions ─────────────────────────────────────────────

def print_menu():
    print("========================================")
    print("           GRADE BUDDY")
    print("========================================")
    print("1. Add subjects")
    print("2. View report")
    print("3. View history")
    print("4. Quit")
    print()


def print_history(history):
    if not history:
        print("No history yet.")
        return
    print("--- Session History ---")
    for i in range(len(history)):
        print(f"[{i + 1}] {history[i]}")
    print("----------------------")


def run():
    subjects = []
    history = []

    while True:
        print_menu()
        choice = input("Your choice: ").strip()

        if choice == "1":
            new_subjects = collect_all_subjects()
            subjects = subjects + new_subjects
            history.append(f"Added {len(new_subjects)} subject(s)")

        elif choice == "2":
            if subjects:
                print_report(subjects)
                history.append("Viewed report")
            else:
                print("No subjects added yet. Choose 1 first.")

        elif choice == "3":
            print_history(history)
            history.append("Viewed history")

        elif choice == "4":
            print("Goodbye! Keep studying hard!")
            break

        else:
            print("Please choose 1, 2, 3 or 4.")


# ── Run ───────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    run()
