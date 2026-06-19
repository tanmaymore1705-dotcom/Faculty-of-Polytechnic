# Grade Buddy — CP4: Main Menu + History

**Module:** 1 Mini-Capstone · **Part:** 4 of 4 · **Time budget:** 60 min

This is the final part. You have a working report card generator. Now you'll
wrap it in a **main menu loop** (same pattern as D15's calculator) and add a
**session history** log (same idea as D15's stretch problem).

After this part, Grade Buddy is a complete, polished program — your **Module 1
capstone submission**.

**Open your `students/<your-username>/grade_buddy.py`** and add the three new
functions below.

---

## What to add

### The menu

```
========================================
           GRADE BUDDY
========================================
1. Add subjects
2. View report
3. View history
4. Quit

Your choice: _
```

If the user types anything other than `1`–`4`, print
`"Please choose 1, 2, 3 or 4."` and show the menu again.

---

### Session history

Before the loop starts, create a `history` list. Every time the user completes
an action, append a string to it:

| Action         | Append                                  |
| -------------- | --------------------------------------- |
| Added subjects | `f"Added {len(new_subjects)} subject(s)"` |
| Viewed report  | `"Viewed report"`                       |
| Viewed history | `"Viewed history"`                      |

---

## The three functions to write

### 1. `print_menu()`

Prints the header and four menu options. No parameters, no return value.

---

### 2. `print_history(history)`

Prints a numbered log of everything done this session.

- If the list is empty: print `"No history yet."`.
- Otherwise:
  ```
  --- Session History ---
  [1] Added 1 subject(s)
  [2] Viewed report
  ----------------------
  ```

**Hint:** `for i in range(len(history)): print(f"[{i + 1}] {history[i]}")`

---

### 3. `run()`

The top-level driver. Replace the `main()` call at the bottom with `run()`.

```python
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
```

The skeleton is **given to you** — implement `print_menu` and `print_history`
so the whole thing works.

**Key lines to understand:**
- `subjects = subjects + new_subjects` — joins two lists, same as `"a" + "b"`.
- `if subjects:` — an empty list is falsy; this guards against an empty report.
- The history append for "Viewed history" runs *after* `print_history`, so it
  shows up on the *next* history view.

---

## Expected session

```
========================================
           GRADE BUDDY
========================================
1. Add subjects
2. View report
3. View history
4. Quit

Your choice: 1
Subject name: Maths
  Mark 1 (0-100): 85
  Mark 2 (0-100): 90
  Mark 3 (0-100): 78
Add another subject? (y/n): n

Your choice: 2

============================================================
                    GRADE REPORT
============================================================
Subject          | M1  | M2  | M3  | Avg  | Grade | Result
------------------------------------------------------------
Maths            |  85 |  90 |  78 | 84.3 |   B   | DISTINCTION
------------------------------------------------------------
Overall Average: 84.3
============================================================

Your choice: 3
--- Session History ---
[1] Added 1 subject(s)
[2] Viewed report
----------------------

Your choice: 4
Goodbye! Keep studying hard!
```

---

## Hints

- `print_menu()` is just `print()` calls — no logic.
- `if not history:` tests whether the list is empty.
- Change `if __name__ == "__main__": main()` at the bottom to call `run()`.

## How to submit

1. Finalise `grade_buddy.py` — it should contain all functions from CP1–CP4.
2. Run the session above and confirm the output matches.
3. Commit + push and open/update your PR. This is your **Module 1 capstone
   submission** — make it clean.

## ★ Stretch

Add an **Edit** option (menu choice `5`):

1. Show subjects numbered.
2. Ask which number to replace.
3. Call `collect_one_subject()` for the new data.
4. Replace with index assignment: `subjects[index] = new_entry`.

This is your first taste of **mutating a list by index** — a key Module 2 topic.
