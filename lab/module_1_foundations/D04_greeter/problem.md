# D4 — Greeter + Tip Calculator

**Module:** 1 (Python Foundations) · **Day:** 4 · **Time budget:** 60 min (lab)

Today you'll write two small programs that take input from the user. Both go in
the same file: `students/<your-username>/D04_greeter.py`.

## Problem 1 — Greeter

Write a function `greet()` that:

1. Asks the user for their name (a string).
2. Asks the user for their age (an integer).
3. Prints a single line in the form:
   `Hi <name>! Next year you will be <age+1>.`

### Expected behaviour

```
Your name? Aisha
Your age? 19
Hi Aisha! Next year you will be 20.
```

## Problem 2 — Tip Calculator

Write a function `tip_calculator()` that:

1. Asks the user for the bill amount (a decimal number).
2. Asks the user for the tip percentage (a decimal number, e.g. `15` means 15%).
3. Prints **two** lines:
   - `Tip: <tip-amount>` — formatted to exactly 2 decimal places.
   - `Total: <bill + tip>` — formatted to exactly 2 decimal places.

### Expected behaviour

```
Bill amount? 850.50
Tip percentage? 12
Tip: 102.06
Total: 952.56
```

## Hints

- `input()` always returns a string. Convert it.
- For whole numbers: `int(input(...))`. For decimals: `float(input(...))`.
- For 2-decimal formatting: `f"{value:.2f}"`.

## How to submit

1. In your fork of `Faculty-of-Polytechnic`, click "Sync fork" to get today's
   starter.
2. Create `students/<your-github-username>/D04_greeter.py`.
3. Copy `starter.py` from this folder into your new file.
4. Implement both `greet()` and `tip_calculator()`.
5. Open a PR against upstream `main`.

## ★ Stretch problem (optional)

Add input validation to `tip_calculator()`: if the user types something that
isn't a number (e.g. `"twelve"`), print `"That's not a number — try again."`
and re-prompt instead of crashing. (Hint: `try/except ValueError` — we'll cover
this properly on D28, but you can peek ahead.)
