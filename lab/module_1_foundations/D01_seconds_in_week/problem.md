# D1 — Seconds in a Week

**Module:** 1 (Python Foundations) · **Day:** 1 · **Time budget:** 30 min

## Problem

Write a Python function called `seconds_in_week()` that returns the number of
seconds in one week as an integer.

## Worked breakdown (think first, code second)

- 60 seconds in a minute
- 60 minutes in an hour
- 24 hours in a day
- 7 days in a week

Multiply them all together.

## Expected behaviour

```python
print(seconds_in_week())
# 604800
```

## How to submit

1. Fork the upstream `Faculty-of-Polytechnic` repo (one-time, on Day 4 onwards).
2. In your fork, create a file at `students/<your-github-username>/D01_seconds_in_week.py`.
3. Copy the contents of `starter.py` into your new file and complete the function.
4. Commit + push to your fork.
5. Open a Pull Request against the upstream `main` branch.

## ★ Stretch

Generalise the function: `seconds_in(weeks=0, days=0, hours=0)` returns the
total seconds across all three parameters.
