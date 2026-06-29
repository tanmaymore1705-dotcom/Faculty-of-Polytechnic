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

#cp4 -->3]run fun
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

__name__ == "__main__":
    run()
