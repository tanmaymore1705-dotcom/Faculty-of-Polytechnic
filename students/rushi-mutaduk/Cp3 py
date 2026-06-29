#cp3 -->0]subject limit
MAX_SUBJECTS=5

#cp3 -->1]collect imfo of all subjects
def collect_all_subjects():
    subjects=[]
    entry=collect_one_subject()
    subjects.append(entry)
    while len(subjects)<MAX_SUBJECTS:
        if ask_yes_no("add another subject? (y/n) -->"):
            entry=collect_one_subject()
            subjects.append(entry)
        else:
            break
    if len(subjects)==MAX_SUBJECTS:
        print("maximum 5 subjects reached !")
    return subjects

#cp3 -->2]build subject row
def build_subject_row(name,m1,m2,m3):
    avg=average_of_three(m1,m2,m3)
    grade=letter_grade(avg)
    result=classify_average(avg)
    return f"{name:<9}|{m1:>3}|{m2:>3}|{m3:>3}|{avg:>4.1f} |{grade:^1}-{result}"

#cp3 -->3]print full report
def print_report(subjects):
    print("="*40)
    print("                    GRADE REPORT")
    print("="*40)
    print("Subject  | M1| M2| M3|Avg|Grade-Result")
    print("-"*40)
    total=0
    for name,m1,m2,m3 in subjects:
        print(build_subject_row(name,m1,m2,m3))
        total=total+average_of_three(m1,m2,m3)
    print("-"*40)
    overall_average=round(total/len(subjects),1)
    print(f"Overall Average: {overall_average}")
    print("="*40)
    
#cp3 -->4]main function
def main():
    print("="*40)
    print("             GRADE BUDDY")
    print("="*40)
    subjects=collect_all_subjects()
    print_report(subjects)
