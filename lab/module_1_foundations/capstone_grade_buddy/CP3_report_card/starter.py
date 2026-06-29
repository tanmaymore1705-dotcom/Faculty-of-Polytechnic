# Grade Buddy — CP3: Report Card
#
# Read the full brief in problem.md.
# Add these four functions to your growing grade_buddy.py file.
#
# CP1 and CP2 functions are given below so you can run this file standalone.


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


# ── CP3: Your four new functions ──────────────────────────────────────────────

MAX_SUBJECTS = 5


def collect_all_subjects():
    # 1. subjects = []
    # 2. entry = collect_one_subject()
    #    subjects.append(entry)
    # 3. while len(subjects) < MAX_SUBJECTS:
    #        if ask_yes_no("Add another subject? (y/n): "):
    #            subjects.append(collect_one_subject())
    #        else:
    #            break
    # 4. if len(subjects) == MAX_SUBJECTS:
    #        print("Maximum 5 subjects reached.")
    # 5. return subjects
    pass


def build_subject_row(name, m1, m2, m3):
    # 1. avg    = average_of_three(m1, m2, m3)
    # 2. grade  = letter_grade(avg)
    # 3. result = classify_result(avg)
    # 4. return a formatted row string, e.g.:
    #    "Maths            |  85 |  90 |  78 | 84.3 |   B   | DISTINCTION"
    # Hint: f"{name:<16}| {m1:>3} | {m2:>3} | {m3:>3} | {avg:<4} | {grade:^5} | {result}"
    pass


def print_report(subjects):
    # 1. Print the header:
    #      ============================================================
    #                          GRADE REPORT
    #      ============================================================
    #      Subject          | M1  | M2  | M3  | Avg  | Grade | Result
    #      ------------------------------------------------------------
    # 2. for name, m1, m2, m3 in subjects:
    #        print(build_subject_row(name, m1, m2, m3))
    # 3. Print "----..." divider
    # 4. Accumulator for overall average:
    #      total = 0
    #      for name, m1, m2, m3 in subjects:
    #          total += average_of_three(m1, m2, m3)
    #      overall = round(total / len(subjects), 1)
    #      print(f"Overall Average: {overall}")
    # 5. Print "====..." closing border
    pass


def main():
    # 1. Print welcome header  ("=" * 40, "       GRADE BUDDY", "=" * 40)
    # 2. subjects = collect_all_subjects()
    # 3. print_report(subjects)
    pass


# ── Run ───────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    main()
