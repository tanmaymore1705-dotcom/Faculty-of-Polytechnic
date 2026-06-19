# Grade Buddy — CP1: Core Functions
#
# Read the full brief in problem.md.
# These are PURE functions: no input(), no print() inside them.
# Each takes values, does maths or logic, and returns a result.
#
# You will keep growing this same file through CP2, CP3, and CP4.


PASS_MARK = 35
DISTINCTION_MARK = 75


def average_of_three(m1, m2, m3):
    # Return the average of the three marks, rounded to 1 decimal place.
    # Hint: (m1 + m2 + m3) / 3, then round(..., 1)
    pass


def classify_result(average):
    # Return "FAIL"        if average < PASS_MARK
    # Return "DISTINCTION" if average >= DISTINCTION_MARK
    # Return "PASS"        otherwise
    # Use the named constants — never write 35 or 75 directly here.
    pass


def letter_grade(average):
    # Return "A" (>=90), "B" (>=80), "C" (>=70), "D" (>=60), or "F" (<60).
    pass


def format_marks(m1, m2, m3):
    # Return a string like "85, 90, 78"
    pass


# ── Quick tests — run this file to check your work ────────────────────────────
if __name__ == "__main__":
    print("-- average_of_three --")
    print(average_of_three(85, 90, 78))   # 84.3
    print(average_of_three(30, 28, 35))   # 31.0
    print(average_of_three(40, 55, 70))   # 55.0

    print("-- classify_result --")
    print(classify_result(84.3))          # DISTINCTION
    print(classify_result(55.0))          # PASS
    print(classify_result(31.0))          # FAIL

    print("-- letter_grade --")
    print(letter_grade(84.3))             # B
    print(letter_grade(55.0))             # F
    print(letter_grade(92.0))             # A

    print("-- format_marks --")
    print(format_marks(85, 90, 78))       # 85, 90, 78
    print(format_marks(30, 28, 35))       # 30, 28, 35
