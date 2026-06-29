pass_mark=35
distinction_mark=75

# cp1 --> 1] average
def average_of_three(m1,m2,m3):
    average=(m1+m2+m3)/3
    return round(average,1)

# cp1 --> 2] classify average
def classify_average(average):
    if average<pass_mark:
        return "Failed"
    elif average>=distinction_mark:
        return "Distinction"
    else:
        return "Pass"

# cp1 --> 3] classify grade
def letter_grade(average):
    if average>=90:
        return "A"
    elif average>=80:
        return "B"
    elif average>=70:
        return "C"
    elif average>=60:
        return "D"
    else:
        return "F"

# cp1 --> 4] make string
def format_marks(m1,m2,m3):
    return f"{m1}, {m2}, {m3}"

# cp1 --> 5] improvement check
def is_improvement(old_average,new_average):
    if new_average>old_average:
        return True
    else:
        return False
        
        
#cp2 -->1]ask text
def ask_text(prompt):
    while True:
        text=input(prompt)
        if text=="":
            print("cant be empty try again !")
        else:
            return text
            
#cp2 -->2]ask marks
def ask_mark(prompt):
    while True:
        text=input(prompt)
        if not text.isdigit():
            print("please enter a whole number !")
            continue
        mark=int(text)
        if 0<=mark<=100:
            return mark
        else:
            print("mark must be between 0 and 100 !")
            
#cp2 -->3]ask yes or no
def ask_yes_no(question):
    while True:
        answer=input(question)
        if answer=="y":
            return True
        elif answer=="n":
            return False
        else:
            print("please type (y/n) !")
            
#cp2 -->4]collect imformatiom for 1 sub
def collect_one_subject():
    name=ask_text("subject name --> ")
    m1=ask_mark("Marks 1 (0-100) --> ")
    m2=ask_mark("Marks 2 (0-100) --> ")
    m3=ask_mark("Marks 3 (0-100) --> ")
    return (name,m1,m2,m3)


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
        total+=average_of_three(m1,m2,m3)
    print("-"*40)
    overall_average=round(total/len(subjects),1)
    print(f"Overall Average: {overall_average}")
    print("="*40)
    
#cp3 -->4]main function
def main():
    print("\n\n")
    print("="*40)
    print("             GRADE BUDDY")
    print("="*40)
    subjects=collect_all_subjects()
    print_report(subjects)
    
    
#cp4 -->1]showing menue
def print_menu():
    print("\n\n")
    print("="*40)
    print("              GRADE BUDDY")
    print("="*40)
    print("1]add subjects")
    print("2]view report")
    print("3]view history")
    print("4]quit")

#cp4 -->2]show history
def print_history(history):
    if not history:
        print("no history yet !")
    else:
        print("-*- Session History -*-")
        for i in range(len(history)):
            print(f"[{i+1}] {history[i]}")
        print("-*-*-*-*-*-*-*-*-*-*-")

#cp4 -->3]main fun
def run():
    subjects=[]
    history=[]
    while True:
        print_menu()
        choice=input("your choice --> ").strip()
        if choice=="1":
            new_subjects=collect_all_subjects()
            subjects=subjects+new_subjects
            history.append(f"Added {len(new_subjects)} subject(s)")
        elif choice=="2":
            if subjects:
                print_report(subjects)
                history.append("Viewed report")
            else:
                print("no subjects added yet select 1 first !")
        elif choice=="3":
            print_history(history)
            history.append("Viewed history")
        elif choice=="4":
            print("GOODBYE ! STAY HARD !")
            break
        else:
            print("Please choose 1/2/3/4 -->")

#cp4 -->4]start execution
if __name__=="__main__":
    run()
