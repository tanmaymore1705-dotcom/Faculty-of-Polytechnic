# Grade Buddy — CP2: Input Helpers

**Module:** 1 Mini-Capstone · **Part:** 2 of 4 · **Time budget:** 60 min

In CP1 you wrote the four core calculation functions. In this part you write the
**input helpers** — functions that ask the user a question and return a clean,
validated answer.

The key pattern here is the **validation loop**: keep asking until the user
types something valid. You used this shape in D8 (`while True` + `break`) and
saw it hinted at in D5's stretch problem. Now you'll apply it properly to every
input your app needs.

**Open your `students/<your-username>/grade_buddy.py`** from CP1 and add the
four new functions below to the **same file**. Do not start a new file.

---

## The four functions to write

### 1. `ask_text(prompt)`

Asks the user with `input(prompt)`. If they press Enter without typing anything,
print `"Can't be empty — try again."` and ask again. Return the non-empty string.

```
ask_text("Subject name: ")
Subject name:               <- user pressed Enter without typing
Can't be empty — try again.
Subject name: Maths
-> returns "Maths"
```

---

### 2. `ask_mark(prompt)`

Asks the user for a whole-number mark from `0` to `100`. Keep asking until:
- the input is a whole number (`str.isdigit()` is your friend), **and**
- it is between `0` and `100` inclusive.

If the input is not a number, print `"Please enter a whole number."`.
If it is a number but out of range, print `"Mark must be between 0 and 100."`.
Return the mark as an `int`.

```
ask_mark("Mark 1 (0-100): ")
Mark 1 (0-100): abc
Please enter a whole number.
Mark 1 (0-100): 150
Mark must be between 0 and 100.
Mark 1 (0-100): 85
-> returns 85
```

**Hint:** Check `text.isdigit()` first. If `True`, convert to `int` and then
check the range. (`str.isdigit()` was mentioned in the D5 stretch hints.)

---

### 3. `ask_yes_no(question)`

Asks `question` and accepts only `"y"` or `"n"` (lowercase). If anything else
is typed, print `'Please type "y" or "n".'` and ask again. Return `True` for
`"y"`, `False` for `"n"`.

```
ask_yes_no("Add another subject? (y/n): ")
Add another subject? (y/n): maybe
Please type "y" or "n".
Add another subject? (y/n): y
-> returns True
```

---

### 4. `collect_one_subject()`

Wires the three helpers together to collect one subject's data:

1. Call `ask_text("Subject name: ")`.
2. Call `ask_mark("  Mark 1 (0-100): ")`.
3. Call `ask_mark("  Mark 2 (0-100): ")`.
4. Call `ask_mark("  Mark 3 (0-100): ")`.
5. Return a **tuple**: `(name, m1, m2, m3)`.

```
collect_one_subject()

Subject name: Maths
  Mark 1 (0-100): 85
  Mark 2 (0-100): 90
  Mark 3 (0-100): 78

-> returns ("Maths", 85, 90, 78)
```

This function has **no loop** — it calls each helper once. The loops live
*inside* the helpers.

---

## Wiring it together — test block

Add this under `if __name__ == "__main__":`:

```python
entry = collect_one_subject()
name, m1, m2, m3 = entry
avg = average_of_three(m1, m2, m3)
result = classify_result(avg)
print(f"Added: {name} | Average: {avg} | {result}")
```

Expected (with Maths 85, 90, 78):
```
Added: Maths | Average: 84.3 | DISTINCTION
```

---

## Hints

- All three validation loops share the same skeleton:
  ```python
  while True:
      text = input(prompt)
      if <valid>:
          return <clean value>
      print("<error message>")
  ```
- **Unpacking a tuple:** `name, m1, m2, m3 = entry` — the same trick from D12.

## How to submit

Add these four functions to your existing `grade_buddy.py` and open/update
your PR against upstream `main`.

## ★ Stretch

Build `collect_all_subjects()` that keeps collecting subjects until the user
says `"n"`, up to a maximum of 5, and returns a **list** of tuples.

```python
subjects = []
subjects.append(x)    # add x to the end
len(subjects)          # number of items
```

You'll need this in CP3 — writing it now means you start CP3 ahead.
