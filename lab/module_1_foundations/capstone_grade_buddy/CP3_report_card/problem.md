# Grade Buddy — CP3: Report Card

**Module:** 1 Mini-Capstone · **Part:** 3 of 4 · **Time budget:** 60 min

You now have eight functions: four that do maths (CP1) and four that handle
input (CP2). In this part you build the **report card** — the formatted output
that makes the app feel real — and wire everything into a working `main()`.

This echoes D14 (formatted report card) and D11 (`main()` as the wiring
function). The big idea is the same: functions that *return* formatted strings,
and only `main()` that *prints* them.

**Open your `students/<your-username>/grade_buddy.py`** and add today's code to
the same file.

---

## The functions to write

### 1. `collect_all_subjects()`

Collects all subjects the user wants to enter. Returns a **list** of tuples
`(name, m1, m2, m3)`.

A **list** grows as you add to it. Operations you need:

```python
subjects = []          # empty list
subjects.append(x)    # add x to the end
len(subjects)          # how many items
```

Algorithm:
1. `subjects = []`
2. `entry = collect_one_subject()` then `subjects.append(entry)`.
3. While `len(subjects) < MAX_SUBJECTS`:
   - `if ask_yes_no("Add another subject? (y/n): "):`
   - collect another and append, or `break`.
4. If `len(subjects) == MAX_SUBJECTS`: print `"Maximum 5 subjects reached."`.
5. Return `subjects`.

---

### 2. `build_subject_row(name, m1, m2, m3)`

Returns one formatted row for the report table as a **string** (does not
print). Use your CP1 functions to compute `avg`, `grade`, and `result`.

Target layout:
```
Maths            |  85 |  90 |  78 | 84.3 |   B   | DISTINCTION
Physics          |  30 |  28 |  35 | 31.0 |   F   | FAIL
```

**F-string padding:**

| Code          | Effect                               |
| ------------- | ------------------------------------ |
| `f"{x:<16}"` | left-align in a field of width 16    |
| `f"{x:>3}"`  | right-align in a field of width 3    |
| `f"{x:^5}"`  | centre in a field of width 5         |

---

### 3. `print_report(subjects)`

Prints the full formatted report card.

Target output:
```
============================================================
                    GRADE REPORT
============================================================
Subject          | M1  | M2  | M3  | Avg  | Grade | Result
------------------------------------------------------------
Maths            |  85 |  90 |  78 | 84.3 |   B   | DISTINCTION
Physics          |  30 |  28 |  35 | 31.0 |   F   | FAIL
------------------------------------------------------------
Overall Average: 57.7
============================================================
```

Algorithm:
1. Print the top border and header lines.
2. `for name, m1, m2, m3 in subjects:` — print each row via `build_subject_row`.
3. Print the divider.
4. Compute the overall average with an accumulator (D7 pattern):
   `total = 0` → loop adding each `average_of_three` → divide by `len(subjects)`.
5. Print overall average and closing border.

---

### 4. `main()`

Wires everything together:

```python
def main():
    print("=" * 40)
    print("       GRADE BUDDY")
    print("=" * 40)
    subjects = collect_all_subjects()
    print_report(subjects)
```

`main()` only calls other functions — no calculation, no loops.

---

## Expected session

```
========================================
       GRADE BUDDY
========================================
Subject name: Maths
  Mark 1 (0-100): 85
  Mark 2 (0-100): 90
  Mark 3 (0-100): 78
Add another subject? (y/n): y
Subject name: Physics
  Mark 1 (0-100): 30
  Mark 2 (0-100): 28
  Mark 3 (0-100): 35
Add another subject? (y/n): n

============================================================
                    GRADE REPORT
============================================================
Subject          | M1  | M2  | M3  | Avg  | Grade | Result
------------------------------------------------------------
Maths            |  85 |  90 |  78 | 84.3 |   B   | DISTINCTION
Physics          |  30 |  28 |  35 | 31.0 |   F   | FAIL
------------------------------------------------------------
Overall Average: 57.7
============================================================
```

---

## Hints

- Build `print_report` in pieces — header, then loop, then footer. Run after
  each step.
- The loop `for name, m1, m2, m3 in subjects:` unpacks each tuple automatically
  — the same trick from D12 and D14's stretch.

## How to submit

Add these functions to your `grade_buddy.py` and open/update your PR. Run the
session above to confirm the output matches.

## ★ Stretch

After the overall average, also print the **best subject** — the one with the
highest average. Use a second accumulator tracking the best average and its
subject name.

```
Overall Average: 57.7
Best Subject: Maths (84.3)
```
