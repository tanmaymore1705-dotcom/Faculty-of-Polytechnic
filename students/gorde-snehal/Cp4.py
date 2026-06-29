#Print_menu

def print_menu():
    print("===== MENU =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Exit")

print_menu()
 

def print_history(history):
    if len(history) == 0:
        print("No history yet.")
    else:
        print("--- Session History ---")
        for i, item in enumerate(history, 1):
            print(f"[{i}] {item}")
        print("----------------------")


history = [
    "Added 1 subject(s)",
    "Viewed report"
]

print_history(history)
