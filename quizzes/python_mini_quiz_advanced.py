questions = [
    # ── Advanced Data Types & Mutability ──
    {
        "question": (
            "What is the output?\n"
            "   x = [1, 2, 3]\n"
            "   y = x\n"
            "   y.append(4)\n"
            "   print(x)"
        ),
        "options": ["A) Error", "B) [1, 2, 3]", "C) [1, 2, 3, 4]", "D) [4]"],
        "answer": "C"
    },
    {
        "question": (
            "What is the output?\n"
            "   a = (1, 2, [3, 4])\n"
            "   a[2].append(5)\n"
            "   print(a)"
        ),
        "options": ["A) Can't modify tuples", "B) Error - tuples are immutable", "C) (1, 2, [3, 4])", "D) (1, 2, [3, 4, 5])"],
        "answer": "D"
    },
    {
        "question": "What's the difference between x = 5 and x = 5.0 in terms of memory?",
        "options": ["A) 5.0 takes less memory", "B) No difference", "C) Depends on Python version", "D) 5 takes less memory than 5.0"],
        "answer": "D"
    },

    # ── Advanced Operators & Precedence ──
    {
        "question": "What is the output of: print(2 + 3 * 4 - 5 / 2)?",
        "options": ["A) 6.0", "B) 9.5", "C) 11.5", "D) 13.5"],
        "answer": "C"
    },
    {
        "question": "What does: 5 == 5.0 and 5 is 5.0 evaluate to?",
        "options": ["A) False, False", "B) True, True", "C) True, False", "D) False, True"],
        "answer": "C"
    },
    {
        "question": "What is the result of: not (True and False or True)?",
        "options": ["A) Error", "B) True", "C) False", "D) None"],
        "answer": "C"
    },

    # ── String Operations & Formatting ──
    {
        "question": (
            "What is the output?\n"
            "   s = 'hello'\n"
            "   print(s[::-1])"
        ),
        "options": ["A) hlelo", "B) Error", "C) olleh", "D) hello"],
        "answer": "C"
    },
    {
        "question": (
            "What does this print?\n"
            "   s = 'Python'\n"
            "   print(s[1:4])"
        ),
        "options": ["A) thon", "B) Pyt", "C) yth", "D) ytho"],
        "answer": "C"
    },
    {
        "question": "What is the output of: '{} {}'.format('hello', 'world')?",
        "options": ["A) hello world", "B) {} {}", "C) Error", "D) {0} {1}"],
        "answer": "A"
    },
    {
        "question": "What does 'hello world'.replace('world', 'Python') return?",
        "options": ["A) helloPython", "B) hello world", "C) hello Python", "D) Error"],
        "answer": "C"
    },

    # ── List/Dict/Set Comprehensions ──
    {
        "question": (
            "What is the output?\n"
            "   result = [x**2 for x in range(4)]\n"
            "   print(result)"
        ),
        "options": ["A) [0, 1, 2, 3, 4]", "B) [0, 1, 2, 3]", "C) [1, 4, 9, 16]", "D) [0, 1, 4, 9]"],
        "answer": "D"
    },
    {
        "question": (
            "What is the output?\n"
            "   result = [x for x in range(5) if x % 2 == 0]\n"
            "   print(result)"
        ),
        "options": ["A) [2, 4]", "B) [1, 3]", "C) [0, 1, 2, 3, 4]", "D) [0, 2, 4]"],
        "answer": "D"
    },
    {
        "question": (
            "What is the output?\n"
            "   d = {x: x**2 for x in range(1, 4)}\n"
            "   print(d)"
        ),
        "options": ["A) {1: 2, 2: 3, 3: 4}", "B) Error", "C) {0: 0, 1: 1, 2: 4}", "D) {1: 1, 2: 4, 3: 9}"],
        "answer": "D"
    },

    # ── Function Parameters & Arguments ──
    {
        "question": (
            "What does this code print?\n"
            "   def func(a, b=10):\n"
            "       return a + b\n"
            "   print(func(5))"
        ),
        "options": ["A) Error", "B) 10", "C) 15", "D) 5"],
        "answer": "C"
    },
    {
        "question": (
            "What is the output?\n"
            "   def func(*args):\n"
            "       return sum(args)\n"
            "   print(func(1, 2, 3, 4))"
        ),
        "options": ["A) Error", "B) 4", "C) 10", "D) (1, 2, 3, 4)"],
        "answer": "C"
    },
    {
        "question": (
            "What does this print?\n"
            "   def func(**kwargs):\n"
            "       return kwargs\n"
            "   print(func(name='John', age=25))"
        ),
        "options": ["A) None", "B) ('name', 'John', 'age', 25)", "C) {'name': 'John', 'age': 25}", "D) Error"],
        "answer": "C"
    },

    # ── Scope & Closures ──
    {
        "question": (
            "What is the output?\n"
            "   x = 10\n"
            "   def func():\n"
            "       x = 20\n"
            "       return x\n"
            "   print(func())\n"
            "   print(x)"
        ),
        "options": ["A) 10, 10", "B) 20, 10", "C) 20, 20", "D) Error"],
        "answer": "B"
    },
    {
        "question": (
            "What is the output?\n"
            "   x = 5\n"
            "   def outer():\n"
            "       def inner():\n"
            "           return x\n"
            "       return inner()\n"
            "   print(outer())"
        ),
        "options": ["A) undefined", "B) 5", "C) None", "D) Error"],
        "answer": "B"
    },

    # ── Lambda & Map/Filter ──
    {
        "question": (
            "What is the output?\n"
            "   f = lambda x: x * 2\n"
            "   print(f(5))"
        ),
        "options": ["A) Error", "B) 10", "C) 2", "D) 5"],
        "answer": "B"
    },
    {
        "question": (
            "What does this print?\n"
            "   result = list(map(lambda x: x**2, [1, 2, 3]))\n"
            "   print(result)"
        ),
        "options": ["A) 6", "B) [1, 4, 9]", "C) Error", "D) [1, 2, 3]"],
        "answer": "B"
    },
    {
        "question": (
            "What is the output?\n"
            "   result = list(filter(lambda x: x > 2, [1, 2, 3, 4]))\n"
            "   print(result)"
        ),
        "options": ["A) Error", "B) [3, 4]", "C) [2, 3, 4]", "D) [1, 2, 3, 4]"],
        "answer": "B"
    },

    # ── Control Flow - Break/Continue ──
    {
        "question": (
            "What is the output?\n"
            "   for i in range(5):\n"
            "       if i == 3:\n"
            "           break\n"
            "       print(i)"
        ),
        "options": ["A) 0 1", "B) 0 1 2 3", "C) 0 1 2", "D) 0 1 2 3 4"],
        "answer": "C"
    },
    {
        "question": (
            "What does this print?\n"
            "   for i in range(5):\n"
            "       if i == 2:\n"
            "           continue\n"
            "       print(i)"
        ),
        "options": ["A) 0 1 3 4", "B) 0 1 2", "C) 1 3 4", "D) 0 1 2 3 4"],
        "answer": "A"
    },

    # ── Dictionary & Set Operations ──
    {
        "question": (
            "What is the output?\n"
            "   d = {'a': 1, 'b': 2}\n"
            "   print(d.get('c', 'default'))"
        ),
        "options": ["A) Error", "B) default", "C) KeyError", "D) None"],
        "answer": "B"
    },
    {
        "question": (
            "What does this print?\n"
            "   s = {1, 2, 2, 3, 3, 3}\n"
            "   print(len(s))"
        ),
        "options": ["A) 9", "B) 3", "C) Error", "D) 6"],
        "answer": "B"
    },
    {
        "question": (
            "What is the output?\n"
            "   d1 = {'a': 1, 'b': 2}\n"
            "   d2 = {'b': 3, 'c': 4}\n"
            "   d1.update(d2)\n"
            "   print(d1)"
        ),
        "options": ["A) {'a': 1, 'b': 2, 'b': 3, 'c': 4}", "B) {'a': 1, 'b': 3, 'c': 4}", "C) {'a': 1, 'b': 2, 'c': 4}", "D) Error"],
        "answer": "B"
    },

    # ── Slicing & Indexing Edge Cases ──
    {
        "question": (
            "What is the output?\n"
            "   lst = [1, 2, 3, 4, 5]\n"
            "   print(lst[-2:])"
        ),
        "options": ["A) [4, 5]", "B) Error", "C) [5]", "D) [3, 4, 5]"],
        "answer": "A"
    },
    {
        "question": (
            "What does this print?\n"
            "   s = 'Python'\n"
            "   print(s[10])"
        ),
        "options": ["A) None", "B) Error - IndexError", "C) ''", "D) n"],
        "answer": "B"
    },

    # ── Boolean Logic & Truthiness ──
    {
        "question": "Which of these is considered FALSY in Python?",
        "options": ["A) [0]", "B) None", "C) []", "D) '0'"],
        "answer": "C"
    },
    {
        "question": (
            "What is the output?\n"
            "   print(bool(''))\n"
            "   print(bool('hello'))"
        ),
        "options": ["A) True, False", "B) True, True", "C) False, True", "D) False, False"],
        "answer": "C"
    },

    # ── Type Conversions & Edge Cases ──
    {
        "question": "What is int(3.9)?",
        "options": ["A) 3", "B) 3.0", "C) Error", "D) 4"],
        "answer": "A"
    },
    {
        "question": "What does int('3.5') return?",
        "options": ["A) 3", "B) '3.5'", "C) Error", "D) 3.5"],
        "answer": "C"
    },
    {
        "question": (
            "What is the output?\n"
            "   x = [1, 2, 3]\n"
            "   print(x + [4])"
        ),
        "options": ["A) [1, 2, 3] + [4]", "B) [5]", "C) [1, 2, 3, 4]", "D) Error"],
        "answer": "C"
    },

    # ── Generators & Iterators Basics ──
    {
        "question": (
            "What is the output?\n"
            "   def gen():\n"
            "       yield 1\n"
            "       yield 2\n"
            "   print(list(gen()))"
        ),
        "options": ["A) (1, 2)", "B) [1, 2]", "C) 1 2", "D) Error"],
        "answer": "B"
    },

    # ── List Aliasing/Copying ──
    {
        "question": (
            "What is the output?\n"
            "   x = [1, 2, 3]\n"
            "   y = x[:]\n"
            "   y.append(4)\n"
            "   print(x)"
        ),
        "options": ["A) [1, 2, 3]", "B) [4]", "C) Error", "D) [1, 2, 3, 4]"],
        "answer": "A"
    },

    # ── Nested Loops & Complex Logic ──
    {
        "question": (
            "What is the output?\n"
            "   count = 0\n"
            "   for i in range(3):\n"
            "       for j in range(2):\n"
            "           count += 1\n"
            "   print(count)"
        ),
        "options": ["A) 5", "B) 2", "C) 6", "D) 3"],
        "answer": "C"
    },
    {
        "question": (
            "What does this print?\n"
            "   result = []\n"
            "   for i in range(3):\n"
            "       for j in range(3):\n"
            "           if i == j:\n"
            "               result.append(i)\n"
            "   print(result)"
        ),
        "options": ["A) []", "B) [0, 1, 1, 2, 2]", "C) [0, 1, 2]", "D) [0, 0, 1, 1, 2, 2]"],
        "answer": "C"
    },

    # ── Unpacking & Zip ──
    {
        "question": (
            "What is the output?\n"
            "   a, b = 1, 2\n"
            "   print(a, b)"
        ),
        "options": ["A) 2 1", "B) (1, 2)", "C) 1 2", "D) Error"],
        "answer": "C"
    },
    {
        "question": (
            "What does this print?\n"
            "   lists = zip([1, 2, 3], ['a', 'b', 'c'])\n"
            "   print(list(lists))"
        ),
        "options": ["A) [1, 2, 3, 'a', 'b', 'c']", "B) [(1, 'a'), (2, 'b'), (3, 'c')]", "C) Error", "D) (1, 'a', 2, 'b', 3, 'c')"],
        "answer": "B"
    },
]


def run_quiz():
    print("=" * 60)
    print("         PYTHON ADVANCED MINI QUIZ (Tougher!)")
    print("=" * 60)
    print(f"Total Questions: {len(questions)}")
    print("Answer each question by typing A, B, C, or D.")
    print("=" * 60)

    score = 0
    incorrect_questions = []

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
            incorrect_questions.append((i, q["question"], q["answer"]))

    print("\n" + "=" * 60)
    print(f"QUIZ COMPLETE! Your score: {score}/{len(questions)}")

    pct = score / len(questions)
    if pct == 1.0:
        print("🏆 PERFECT! You are a Python master!")
    elif pct >= 0.85:
        print("🎉 Excellent work! Advanced Python concepts are solid.")
    elif pct >= 0.70:
        print("👍 Very good! Keep studying edge cases and tricky behavior.")
    elif pct >= 0.55:
        print("📚 Good progress! Review the concepts you missed.")
    elif pct >= 0.40:
        print("💪 Keep practicing! Study Python's subtleties more deeply.")
    else:
        print("🔄 Review the fundamentals and work through more examples.")

    if incorrect_questions:
        print("\nQuestions you missed:")
        for q_num, question, correct in incorrect_questions[:5]:
            print(f"  Q{q_num}: Answer {correct}")

    print("=" * 60)


if __name__ == "__main__":
    run_quiz()
