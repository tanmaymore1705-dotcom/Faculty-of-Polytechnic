questions = [
    # ── Data Types & Variables ──
    {
        "question": "What is the output of: print(type(3.14))?",
        "options": ["A) <class 'int'>", "B) <class 'float'>", "C) <class 'str'>", "D) <class 'double'>"],
        "answer": "B"
    },
    {
        "question": "Which of the following is the correct way to declare a variable in Python?",
        "options": ["A) int x = 5", "B) var x = 5", "C) x = 5", "D) declare x = 5"],
        "answer": "C"
    },
    {
        "question": "What is the data type of the value True in Python?",
        "options": ["A) str", "B) int", "C) bool", "D) bit"],
        "answer": "C"
    },
    {
        "question": "Which of the following creates a STRING in Python?",
        "options": ['A) x = 42', 'B) x = 3.14', 'C) x = "hello"', "D) x = [1, 2, 3]"],
        "answer": "C"
    },

    # ── Operators ──
    {
        "question": "What will 10 % 3 evaluate to?",
        "options": ["A) 3", "B) 1", "C) 0", "D) 3.33"],
        "answer": "B"
    },
    {
        "question": "What is the result of 2 ** 4 in Python?",
        "options": ["A) 8", "B) 16", "C) 6", "D) 24"],
        "answer": "B"
    },
    {
        "question": "Which operator is used for integer (floor) division in Python?",
        "options": ["A) /", "B) %", "C) //", "D) \\"],
        "answer": "C"
    },

    # ── Strings & Built-ins ──
    {
        "question": "What does len('hello') return?",
        "options": ["A) 4", "B) 6", "C) 5", "D) Error"],
        "answer": "C"
    },
    {
        "question": "Which method converts a string to ALL UPPERCASE?",
        "options": ["A) str.upper()", "B) str.capitalize()", "C) str.title()", "D) str.big()"],
        "answer": "A"
    },
    {
        "question": "What is the output of 'Python'[0]?",
        "options": ["A) P", "B) y", "C) Py", "D) Error"],
        "answer": "A"
    },

    # ── Collections ──
    {
        "question": "Which of the following is a valid Python list?",
        "options": ["A) (1, 2, 3)", "B) {1, 2, 3}", "C) [1, 2, 3]", "D) <1, 2, 3>"],
        "answer": "C"
    },
    {
        "question": "What method adds an item to the END of a list?",
        "options": ["A) list.add()", "B) list.insert()", "C) list.push()", "D) list.append()"],
        "answer": "D"
    },
    {
        "question": "Which collection type is IMMUTABLE (cannot be changed after creation)?",
        "options": ["A) list", "B) tuple", "C) dict", "D) set"],
        "answer": "B"
    },

    # ── Control Flow ──
    {
        "question": "What is the correct way to add a comment in Python?",
        "options": ["A) // This is a comment", "B) /* This is a comment */",
                    "C) <!-- comment -->", "D) # This is a comment"],
        "answer": "D"
    },
    {
        "question": (
            "What does the following code print?\n"
            "   x = 5\n"
            "   if x > 3:\n"
            "       print('yes')\n"
            "   else:\n"
            "       print('no')"
        ),
        "options": ["A) no", "B) yes", "C) 5", "D) Error"],
        "answer": "B"
    },
    {
        "question": "Which loop is used when the number of iterations is NOT known in advance?",
        "options": ["A) for loop", "B) while loop", "C) do-while loop", "D) repeat loop"],
        "answer": "B"
    },
    {
        "question": (
            "What does this code print?\n"
            "   for i in range(3):\n"
            "       print(i)"
        ),
        "options": ["A) 1 2 3", "B) 0 1 2 3", "C) 0 1 2", "D) 1 2"],
        "answer": "C"
    },

    # ── Functions & I/O ──
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": ["A) function", "B) fun", "C) def", "D) define"],
        "answer": "C"
    },
    {
        "question": "Which function is used to get input from the user?",
        "options": ["A) get()", "B) scan()", "C) read()", "D) input()"],
        "answer": "D"
    },
    {
        "question": "How do you convert the string '42' to an integer?",
        "options": ["A) str('42')", "B) float('42')", "C) int('42')", "D) num('42')"],
        "answer": "C"
    },
]


def run_quiz():
    print("=" * 55)
    print("           PYTHON MINI QUIZ")
    print("=" * 55)
    print(f"Total Questions: {len(questions)}")
    print("Answer each question by typing A, B, C, or D.")
    print("=" * 55)

    score = 0

    for i, q in enumerate(questions, start=1):
        print(f"\nQ{i}. {q['question']}")
        for option in q["options"]:
            print(f"   {option}")

        while True:
            answer = input("\nYour answer (A/B/C/D): ").strip().upper()
            if answer in ("A", "B", "C", "D"):
                break
            print("Invalid input. Please enter A, B, C, or D.")

        if answer == q["answer"]:
            print("✓ Correct!")
            score += 1
        else:
            print(f"✗ Wrong! The correct answer was {q['answer']}.")

    print("\n" + "=" * 55)
    print(f"QUIZ COMPLETE! Your score: {score}/{len(questions)}")

    pct = score / len(questions)
    if pct == 1.0:
        print("🏆 Perfect score! Outstanding!")
    elif pct >= 0.8:
        print("🎉 Excellent! Great job!")
    elif pct >= 0.6:
        print("👍 Good effort! Review the topics you missed.")
    elif pct >= 0.4:
        print("📚 Keep practising — you're getting there!")
    else:
        print("💪 Don't give up! Go through the lectures and try again.")

    print("=" * 55)


if __name__ == "__main__":
    run_quiz()
