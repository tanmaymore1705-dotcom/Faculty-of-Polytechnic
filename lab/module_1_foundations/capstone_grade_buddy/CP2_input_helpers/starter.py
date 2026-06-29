# Grade Buddy — CP2: Input Helpers
#
# Read the full brief in problem.md.
# Add these four functions to your growing grade_buddy.py file.
#
# The CP1 functions are given below so you can run this file standalone
# while developing. When you copy into grade_buddy.py, keep only ONE copy
# of each function — no duplicates.


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


# ── CP2: Your four new functions ──────────────────────────────────────────────

def ask_text(prompt):
    # Keep asking until the user types something non-empty.
    # If they press Enter without typing: print "Can't be empty — try again."
    # Return the non-empty string.
    #
    # Skeleton:
    #   while True:
    #       text = input(prompt)
    #       if text:           <- a non-empty string is truthy
    #           return text
    #       print("Can't be empty — try again.")
    pass


def ask_mark(prompt):
    # Keep asking until the user types a whole number between 0 and 100.
    # - Not a number  -> print "Please enter a whole number."
    # - Out of range  -> print "Mark must be between 0 and 100."
    # Return the mark as an int.
    # Hint: use text.isdigit() to check before converting with int()
    pass


def ask_yes_no(question):
    # Keep asking until the user types "y" or "n".
    # Anything else -> print 'Please type "y" or "n".'
    # Return True for "y", False for "n".
    pass


def collect_one_subject():
    # 1. name = ask_text("Subject name: ")
    # 2. m1   = ask_mark("  Mark 1 (0-100): ")
    # 3. m2   = ask_mark("  Mark 2 (0-100): ")
    # 4. m3   = ask_mark("  Mark 3 (0-100): ")
    # 5. return (name, m1, m2, m3)
    pass


# ── Quick test ────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    print("Enter one subject:")
    entry = collect_one_subject()
    name, m1, m2, m3 = entry
    avg = average_of_three(m1, m2, m3)
    result = classify_result(avg)
    print(f"Added: {name} | Average: {avg} | {result}")
