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
        "options": ["A) [1, 2, 3]", "B) [1, 2, 3, 4]", "C) Error", "D) [4]"],
        "answer": "B"
    },
    {
        "question": (
            "What is the output?\n"
            "   a = (1, 2, [3, 4])\n"
            "   a[2].append(5)\n"
            "   print(a)"
        ),
        "options": ["A) Error - tuples are immutable", "B) (1, 2, [3, 4, 5])", "C) (1, 2, [3, 4])", "D) Can't modify tuples"],
        "answer": "B"
    },
    {
        "question": "What's the difference between x = 5 and x = 5.0 in terms of memory?",
        "options": ["A) No difference", "B) 5 takes less memory than 5.0", "C) 5.0 takes less memory", "D) Depends on Python version"],
        "answer": "B"
    },

    # ── Advanced Operators & Precedence ──
    {
        "question": "What is the output of: print(2 + 3 * 4 - 5 / 2)?",
        "options": ["A) 9.5", "B) 11.5", "C) 13.5", "D) 6.0"],
        "answer": "B"
    },
    {
        "question": "What does: 5 == 5.0 and 5 is 5.0 evaluate to?",
        "options": ["A) True, True", "B) True, False", "C) False, True", "D) False, False"],
        "answer": "B"
    },
    {
        "question": "What is the result of: not (True and False or True)?",
        "options": ["A) True", "B) False", "C) None", "D) Error"],
        "answer": "B"
    },

    # ── String Operations & Formatting ──
    {
        "question": (
            "What is the output?\n"
            "   s = 'hello'\n"
            "   print(s[::-1])"
        ),
        "options": ["A) hello", "B) olleh", "C) hlelo", "D) Error"],
        "answer": "B"
    },
    {
        "question": (
            "What does this print?\n"
            "   s = 'Python'\n"
            "   print(s[1:4])"
        ),
        "options": ["A) Pyt", "B) yth", "C) ytho", "D) thon"],
        "answer": "B"
    },
    {
        "question": "What is the output of: '{} {}'.format('hello', 'world')?",
        "options": ["A) hello world", "B) {0} {1}", "C) {} {}", "D) Error"],
        "answer": "A"
    },
    {
        "question": "What does 'hello world'.replace('world', 'Python') return?",
        "options": ["A) hello Python", "B) hello world", "C) helloPython", "D) Error"],
        "answer": "A"
    },

    # ── List/Dict/Set Comprehensions ──
    {
        "question": (
            "What is the output?\n"
            "   result = [x**2 for x in range(4)]\n"
            "   print(result)"
        ),
        "options": ["A) [0, 1, 4, 9]", "B) [0, 1, 2, 3]", "C) [1, 4, 9, 16]", "D) [0, 1, 2, 3, 4]"],
        "answer": "A"
    },
    {
        "question": (
            "What is the output?\n"
            "   result = [x for x in range(5) if x % 2 == 0]\n"
            "   print(result)"
        ),
        "options": ["A) [0, 2, 4]", "B) [1, 3]", "C) [0, 1, 2, 3, 4]", "D) [2, 4]"],
        "answer": "A"
    },
    {
        "question": (
            "What is the output?\n"
            "   d = {x: x**2 for x in range(1, 4)}\n"
            "   print(d)"
        ),
        "options": ["A) {1: 1, 2: 4, 3: 9}", "B) {1: 2, 2: 3, 3: 4}", "C) {0: 0, 1: 1, 2: 4}", "D) Error"],
        "answer": "A"
    },

    # ── Function Parameters & Arguments ──
    {
        "question": (
            "What does this code print?\n"
            "   def func(a, b=10):\n"
            "       return a + b\n"
            "   print(func(5))"
        ),
        "options": ["A) 5", "B) 15", "C) Error", "D) 10"],
        "answer": "B"
    },
    {
        "question": (
            "What is the output?\n"
            "   def func(*args):\n"
            "       return sum(args)\n"
            "   print(func(1, 2, 3, 4))"
        ),
        "options": ["A) (1, 2, 3, 4)", "B) 10", "C) Error", "D) 4"],
        "answer": "B"
    },
    {
        "question": (
            "What does this print?\n"
            "   def func(**kwargs):\n"
            "       return kwargs\n"
            "   print(func(name='John', age=25))"
        ),
        "options": ["A) Error", "B) ('name', 'John', 'age', 25)", "C) {'name': 'John', 'age': 25}", "D) None"],
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
        "options": ["A) 20, 20", "B) 20, 10", "C) 10, 10", "D) Error"],
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
        "options": ["A) Error", "B) 5", "C) None", "D) undefined"],
        "answer": "B"
    },

    # ── Lambda & Map/Filter ──
    {
        "question": (
            "What is the output?\n"
            "   f = lambda x: x * 2\n"
            "   print(f(5))"
        ),
        "options": ["A) 5", "B) 10", "C) Error", "D) 2"],
        "answer": "B"
    },
    {
        "question": (
            "What does this print?\n"
            "   result = list(map(lambda x: x**2, [1, 2, 3]))\n"
            "   print(result)"
        ),
        "options": ["A) [1, 2, 3]", "B) [1, 4, 9]", "C) 6", "D) Error"],
        "answer": "B"
    },
    {
        "question": (
            "What is the output?\n"
            "   result = list(filter(lambda x: x > 2, [1, 2, 3, 4]))\n"
            "   print(result)"
        ),
        "options": ["A) [1, 2, 3, 4]", "B) [3, 4]", "C) [2, 3, 4]", "D) Error"],
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
        "options": ["A) 0 1 2", "B) 0 1 2 3", "C) 0 1 2 3 4", "D) 0 1"],
        "answer": "A"
    },
    {
        "question": (
            "What does this print?\n"
            "   for i in range(5):\n"
            "       if i == 2:\n"
            "           continue\n"
            "       print(i)"
        ),
        "options": ["A) 0 1 3 4", "B) 0 1 2 3 4", "C) 0 1 2", "D) 1 3 4"],
        "answer": "A"
    },

    # ── Dictionary & Set Operations ──
    {
        "question": (
            "What is the output?\n"
            "   d = {'a': 1, 'b': 2}\n"
            "   print(d.get('c', 'default'))"
        ),
        "options": ["A) None", "B) default", "C) Error", "D) KeyError"],
        "answer": "B"
    },
    {
        "question": (
            "What does this print?\n"
            "   s = {1, 2, 2, 3, 3, 3}\n"
            "   print(len(s))"
        ),
        "options": ["A) 6", "B) 3", "C) Error", "D) 9"],
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
        "options": ["A) {'a': 1, 'b': 2, 'c': 4}", "B) {'a': 1, 'b': 3, 'c': 4}", "C) Error", "D) {'a': 1, 'b': 2, 'b': 3, 'c': 4}"],
        "answer": "B"
    },

    # ── Slicing & Indexing Edge Cases ──
    {
        "question": (
            "What is the output?\n"
            "   lst = [1, 2, 3, 4, 5]\n"
            "   print(lst[-2:])"
        ),
        "options": ["A) [4, 5]", "B) [3, 4, 5]", "C) [5]", "D) Error"],
        "answer": "A"
    },
    {
        "question": (
            "What does this print?\n"
            "   s = 'Python'\n"
            "   print(s[10])"
        ),
        "options": ["A) n", "B) Error - IndexError", "C) None", "D) ''"],
        "answer": "B"
    },

    # ── Boolean Logic & Truthiness ──
    {
        "question": "Which of these is considered FALSY in Python?",
        "options": ["A) '0'", "B) [0]", "C) []", "D) None"],
        "answer": "C"
    },
    {
        "question": (
            "What is the output?\n"
            "   print(bool(''))\n"
            "   print(bool('hello'))"
        ),
        "options": ["A) True, True", "B) False, False", "C) False, True", "D) True, False"],
        "answer": "C"
    },

    # ── Type Conversions & Edge Cases ──
    {
        "question": "What is int(3.9)?",
        "options": ["A) 3", "B) 4", "C) 3.0", "D) Error"],
        "answer": "A"
    },
    {
        "question": "What does int('3.5') return?",
        "options": ["A) 3", "B) 3.5", "C) Error", "D) '3.5'"],
        "answer": "C"
    },
    {
        "question": (
            "What is the output?\n"
            "   x = [1, 2, 3]\n"
            "   print(x + [4])"
        ),
        "options": ["A) [1, 2, 3, 4]", "B) Error", "C) [5]", "D) [1, 2, 3] + [4]"],
        "answer": "A"
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
        "options": ["A) Error", "B) [1, 2]", "C) (1, 2)", "D) 1 2"],
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
        "options": ["A) [1, 2, 3, 4]", "B) [1, 2, 3]", "C) Error", "D) [4]"],
        "answer": "B"
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
        "options": ["A) 3", "B) 2", "C) 6", "D) 5"],
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
        "options": ["A) [0, 1, 2]", "B) [0, 0, 1, 1, 2, 2]", "C) [0, 1, 1, 2, 2]", "D) []"],
        "answer": "A"
    },

    # ── Unpacking & Zip ──
    {
        "question": (
            "What is the output?\n"
            "   a, b = 1, 2\n"
            "   print(a, b)"
        ),
        "options": ["A) 1 2", "B) (1, 2)", "C) Error", "D) 2 1"],
        "answer": "A"
    },
    {
        "question": (
            "What does this print?\n"
            "   lists = zip([1, 2, 3], ['a', 'b', 'c'])\n"
            "   print(list(lists))"
        ),
        "options": ["A) Error", "B) [(1, 'a'), (2, 'b'), (3, 'c')]", "C) [1, 2, 3, 'a', 'b', 'c']", "D) (1, 'a', 2, 'b', 3, 'c')"],
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
