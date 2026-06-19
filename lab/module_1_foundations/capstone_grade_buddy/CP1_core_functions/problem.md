# Grade Buddy — CP1: Core Functions

**Module:** 1 Mini-Capstone · **Part:** 1 of 4 · **Time budget:** 60 min

Welcome to **Grade Buddy** — a command-line app that lets a student track their
test scores for multiple subjects and view a formatted report card.

Over the next four labs you will build it piece by piece. By CP4 you will have
a complete, polished program. Each part adds one layer:

| Part | What you build             | Skills from         |
| ---- | -------------------------- | ------------------- |
| CP1  | Core calculation functions | D1, D6, D7, D11     |
| CP2  | Input helpers + collect    | D4, D8, D10, D11    |
| CP3  | Report card + `main()`     | D5, D11, D13, D14   |
| CP4  | Main menu + history        | D8, D10, D13, D15   |

**Your single file** for the whole capstone is
`students/<your-username>/grade_buddy.py`. You will keep adding to that same
file through all four parts.

---

## This part: Core Functions

You will write **four pure functions** — they take numbers or strings as
parameters and `return` a result. No `input()` and no `print()` inside them.
Everything you write here will be reused in CP2, CP3, and CP4.

---

### 1. `average_of_three(m1, m2, m3)`

Takes three marks (integers 0–100) and returns their average as a float,
rounded to **1 decimal place**.

```python
print(average_of_three(85, 90, 78))  # 84.3
print(average_of_three(30, 28, 35))  # 31.0
print(average_of_three(40, 55, 70))  # 55.0
```

**Hint:** Sum the three marks, divide by `3`, then wrap in `round(..., 1)`.

---

### 2. `classify_result(average)`

Takes the average and returns a result string using the same thresholds as D14:

| Average               | Returns         |
| --------------------- | --------------- |
| `< PASS_MARK`         | `"FAIL"`        |
| `>= PASS_MARK`        | `"PASS"`        |
| `>= DISTINCTION_MARK` | `"DISTINCTION"` |

Use the named constants already declared at the top of the starter
(`PASS_MARK = 35`, `DISTINCTION_MARK = 75`) — never hard-code `35` or `75`
inside the function.

```python
print(classify_result(84.3))  # DISTINCTION
print(classify_result(55.0))  # PASS
print(classify_result(31.0))  # FAIL
```

**Hint:** Check the lowest band first (`< PASS_MARK`), then the highest
(`>= DISTINCTION_MARK`), and let `else` handle everything in between.

---

### 3. `letter_grade(average)`

Returns the letter grade for an average — the same scale you wrote in D6:

| Average   | Grade |
| --------- | ----- |
| `>= 90`   | `"A"` |
| `>= 80`   | `"B"` |
| `>= 70`   | `"C"` |
| `>= 60`   | `"D"` |
| `< 60`    | `"F"` |

```python
print(letter_grade(84.3))  # B
print(letter_grade(55.0))  # F
print(letter_grade(92.0))  # A
```

---

### 4. `format_marks(m1, m2, m3)`

Returns a single string with the three marks separated by `, `.

```python
print(format_marks(85, 90, 78))  # 85, 90, 78
print(format_marks(30, 28, 35))  # 30, 28, 35
```

**Hint:** One `return` with an f-string is all you need.

---

## Hints

- All four functions are short — most are 2–4 lines.
- Run the file after each function to check the test outputs at the bottom
  match the expected values.

## How to submit

1. In your fork of `Faculty-of-Polytechnic`, click "Sync fork".
2. Create `students/<your-github-username>/grade_buddy.py`.
3. Copy `starter.py` from this folder into your new file.
4. Implement all four functions.
5. Run the file — every test line should match.
6. Commit + push, then open a PR against upstream `main`.

## ★ Stretch

Add a fifth function: `is_improvement(old_avg, new_avg)` that returns `True`
if `new_avg` is strictly greater than `old_avg`, `False` otherwise.

```python
print(is_improvement(55.0, 62.0))  # True
print(is_improvement(70.0, 65.0))  # False
print(is_improvement(80.0, 80.0))  # False
```
