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
