# Course Scaffold + D4 Go-Live Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Restructure the `Faculty-of-Polytechnic` repo per `syllabus/COURSE_DESIGN.md`, produce a student-facing interactive course overview page, refresh the README, and deliver the Day 4 lecture deck + Day 4 lab — so faculty can teach Monday morning's D4 session with the new structure already live.

**Architecture:** Pure content artifacts — HTML slide decks, Python starter files, Markdown documentation. No code dependencies, no automated test suites. "Verification" means: HTML files render correctly in a browser, Python starters parse without syntax errors, Markdown previews cleanly on GitHub.

**Tech Stack:** Static HTML/CSS/JS for decks (no build step), Python 3.x for lab problems, Markdown for documentation, git for version control.

**Visual style anchor:** All new HTML artifacts MUST match the visual style of the existing `lecture_presentations/M1D2.html` and `M1D3.html`. Read those files first before building any new HTML — they define the dark theme, IBM Plex font family, cyan accent palette, fixed 1280×720 stage, slide entrance animations, and HUD controls.

---

## File Map

**Create (new files):**
- `lab/module_1_foundations/D01_seconds_in_week/problem.md`
- `lab/module_1_foundations/D01_seconds_in_week/starter.py`
- `lab/module_1_foundations/D04_greeter/problem.md`
- `lab/module_1_foundations/D04_greeter/starter.py`
- `lab/module_1_foundations/D04_greeter/example_run.txt`
- `lab/module_2_practice/.gitkeep`
- `lab/module_3_capstone/.gitkeep`
- `students/.gitkeep`
- `quizzes/.gitkeep`
- `_dev/helpers/.gitkeep`
- `_dev/samples/.gitkeep`
- `syllabus/COURSE_PLAN.html` (student-facing interactive overview)
- `lecture_presentations/M1D4.html` (Day 4 lecture deck)

**Modify (existing files):**
- `README.md` (full rewrite)
- `syllabus/blockchain-syllabus.html` (add deprecation banner at top)
- `problem_1.py` (add SUPERSEDED comment at top)

**Delete:**
- `lab/problem_1.py` (orphan duplicate of root `problem_1.py`; not referenced by any merged PR)

**Do not touch (already finalised):**
- `syllabus/COURSE_DESIGN.md` (the spec)
- `lecture_presentations/M1D2.html`
- `lecture_presentations/M1D3.html`
- `syllabus/program_structure_instructions.pdf`

---

## Task 1: Scaffold new directory structure and migrate Day 1 lab

**Files:**
- Create: `lab/module_1_foundations/D01_seconds_in_week/problem.md`
- Create: `lab/module_1_foundations/D01_seconds_in_week/starter.py`
- Create: `lab/module_2_practice/.gitkeep`
- Create: `lab/module_3_capstone/.gitkeep`
- Create: `students/.gitkeep`
- Create: `quizzes/.gitkeep`
- Create: `_dev/helpers/.gitkeep`
- Create: `_dev/samples/.gitkeep`

- [ ] **Step 1: Create the new directory tree**

```bash
cd "/home/ssd/Documents/Lectures/FOP Repo/Faculty-of-Polytechnic"
mkdir -p lab/module_1_foundations/D01_seconds_in_week
mkdir -p lab/module_2_practice
mkdir -p lab/module_3_capstone
mkdir -p students
mkdir -p quizzes
mkdir -p _dev/helpers
mkdir -p _dev/samples
```

- [ ] **Step 2: Add `.gitkeep` files so empty directories are tracked**

```bash
touch lab/module_2_practice/.gitkeep
touch lab/module_3_capstone/.gitkeep
touch students/.gitkeep
touch quizzes/.gitkeep
touch _dev/helpers/.gitkeep
touch _dev/samples/.gitkeep
```

- [ ] **Step 3: Create `lab/module_1_foundations/D01_seconds_in_week/problem.md`** with this content:

```markdown
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
```

- [ ] **Step 4: Create `lab/module_1_foundations/D01_seconds_in_week/starter.py`** with this content:

```python
# D1 — Seconds in a Week
#
# Write a function that returns the number of seconds in one week.
# 60 seconds * 60 minutes * 24 hours * 7 days

def seconds_in_week():
    # Replace `pass` with your implementation.
    pass


if __name__ == "__main__":
    print(seconds_in_week())
```

- [ ] **Step 5: Verify the directory tree was created correctly**

Run: `find . -path ./.git -prune -o -type d -print | grep -E "lab|students|quizzes|_dev" | sort`

Expected output includes:
```
./_dev
./_dev/helpers
./_dev/samples
./lab
./lab/module_1_foundations
./lab/module_1_foundations/D01_seconds_in_week
./lab/module_2_practice
./lab/module_3_capstone
./quizzes
./students
```

- [ ] **Step 6: Verify the starter file parses as valid Python**

Run: `python3 -m py_compile lab/module_1_foundations/D01_seconds_in_week/starter.py`
Expected: command exits with code 0, no output.

- [ ] **Step 7: Stage and commit**

```bash
git add lab/ students/ quizzes/ _dev/
git commit -m "scaffold: add new lab/students/quizzes/_dev directory structure and migrate D1"
```

---

## Task 2: Mark old artifacts as superseded

**Files:**
- Modify: `problem_1.py` (add header comment)
- Modify: `syllabus/blockchain-syllabus.html` (add deprecation banner)
- Delete: `lab/problem_1.py` (orphan duplicate)

- [ ] **Step 1: Add a SUPERSEDED header to root `problem_1.py`**

Read the current file, then prepend this comment block above the existing content (do not delete or modify the existing function — students' merged PR history depends on it).

The new file content should start with this block, followed by the existing code:

```python
# ─────────────────────────────────────────────────────────────────────────────
# SUPERSEDED — KEPT FOR HISTORICAL PR REFERENCE
#
# This file is the original Day 1 problem and is preserved so existing student
# PR history remains valid. New submissions should go to:
#
#   lab/module_1_foundations/D01_seconds_in_week/
#
# See syllabus/COURSE_DESIGN.md for the active course plan.
# ─────────────────────────────────────────────────────────────────────────────

```

- [ ] **Step 2: Delete the orphan `lab/problem_1.py`**

This file is a stray duplicate from an early commit. No merged PRs reference it (PR #30 et al. modified the *root* `problem_1.py`, not this one).

```bash
rm lab/problem_1.py
```

- [ ] **Step 3: Add deprecation banner to `syllabus/blockchain-syllabus.html`**

The file currently has its content inside `<body>`. Locate the first child element under `<body>` and insert a banner `<div>` immediately above it. Use this exact HTML, which inlines its styles so it doesn't depend on the file's existing CSS:

```html
<div style="position:fixed; top:0; left:0; right:0; z-index:9999; background:#FFD43B; color:#0A0A0F; font-family:system-ui,sans-serif; font-size:14px; font-weight:600; text-align:center; padding:10px 16px; border-bottom:2px solid #0A0A0F;">
  ⚠ DEPRECATED — This blockchain-heavy syllabus was scrapped on 2026-05-29. The active course plan is now <a href="COURSE_DESIGN.md" style="color:#0A0A0F; text-decoration:underline;">syllabus/COURSE_DESIGN.md</a>. This page is kept only as historical reference.
</div>
```

- [ ] **Step 4: Verify the modified files**

Run: `head -15 problem_1.py`
Expected: the SUPERSEDED comment block appears first, followed by the original `# Solve the following problem:` line.

Run: `grep -c "DEPRECATED" syllabus/blockchain-syllabus.html`
Expected: `1`

Run: `ls lab/problem_1.py 2>&1`
Expected: error message (file no longer exists).

- [ ] **Step 5: Stage and commit**

```bash
git add problem_1.py syllabus/blockchain-syllabus.html
git rm lab/problem_1.py
git commit -m "chore: mark legacy syllabus and Day 1 problem files as superseded"
```

---

## Task 3: Rewrite README.md

**Files:**
- Modify: `README.md` (full rewrite)

- [ ] **Step 1: Replace the entire contents of `README.md`** with this content:

```markdown
# Faculty of Polytechnic — Python in 8 Weeks

A 2-month introductory Python course for diploma CS students. Designed for
absolute beginners — variables, loops, functions, collections, files,
errors — finishing with a small Polkadot-themed "tiny blockchain" capstone
implemented entirely in Python.

> **Active course plan:** [`syllabus/COURSE_DESIGN.md`](syllabus/COURSE_DESIGN.md)
> **Interactive overview:** open `syllabus/COURSE_PLAN.html` in a browser

---

## Schedule

- **Mon–Fri**, 8 weeks (~40 working days)
- 09:00 – 10:15 — Lecture (slide deck under `lecture_presentations/`)
- 11:00 – 12:00 — Practical lab (problems under `lab/`)

## Repository map

| Path | What lives here |
|------|-----------------|
| `lecture_presentations/M{module}D{day}.html` | The slide deck for each lecture day |
| `lab/module_{n}_{name}/D{NN}_{slug}/` | Each day's lab problem (`problem.md` + `starter.py`) |
| `students/<github-username>/` | **Each student's personal workspace** — solutions live here |
| `quizzes/` | The 3 biweekly mini-quizzes + final mini-test |
| `syllabus/COURSE_DESIGN.md` | The full course plan (design doc) |
| `syllabus/COURSE_PLAN.html` | Student-facing interactive course overview |
| `syllabus/blockchain-syllabus.html` | Historical reference (deprecated 2026-05-29) |

## How students submit work

The PR workflow is **fork + personal folder**:

1. **One-time:** Click **Fork** at the top of this repo on github.com.
2. **For each lab problem:**
   - Click **"Sync fork"** on your fork's homepage to get today's new starter.
   - Open your fork in [GitHub Codespaces](https://github.com/features/codespaces)
     (`Code → Codespaces → Create codespace`) — this is a free in-browser VS
     Code with Python already installed.
   - Create a new file at `students/<your-github-username>/D{NN}_{slug}.py`.
   - Copy the day's `starter.py` into it and solve the problem.
   - Commit + push from VS Code's Source Control panel.
   - Open a Pull Request against the upstream `main` branch.
3. Faculty reviews and merges your PR.

Over 8 weeks each student accumulates ~30 files in their `students/<username>/`
folder — a visible portfolio on their GitHub profile.

## How faculty work

- New lab content (deck + lab folder) is built the **weekend before** each
  week so we can adjust based on what's landing in the classroom.
- Lab review during the 10:15–11:00 break: skim PRs, leave a one-line
  comment, merge when correct.
- `solutions/` (on a separate `solutions` branch, faculty-only) mirrors the
  `lab/` structure with reference solutions.

## Assessment shape

- 20% — Daily PR participation
- 25% — 5 Friday mini-projects
- 15% — 3 biweekly mini-quizzes
- 15% — Final mini-test (D39)
- 25% — Capstone Tiny Blockchain (Module 3)

No formal external exam. See `syllabus/COURSE_DESIGN.md` for the full design.
```

- [ ] **Step 2: Verify the README renders cleanly**

Run: `wc -l README.md`
Expected: ~60–70 lines.

Run: `grep -c "students/<github-username>" README.md`
Expected: at least 2.

- [ ] **Step 3: Commit**

```bash
git add README.md
git commit -m "docs: rewrite README to describe the 8-week Python course and fork-based PR flow"
```

---

## Task 4: Build `syllabus/COURSE_PLAN.html` — student-facing interactive overview

**Files:**
- Create: `syllabus/COURSE_PLAN.html`

This is a single self-contained HTML page (no build step, no external JS frameworks) modelled on the *interaction pattern* of `syllabus/blockchain-syllabus.html` (module tabs, day cards) but using the *visual style* of `lecture_presentations/M1D2.html` (dark theme, IBM Plex fonts, cyan accents).

- [ ] **Step 1: Read the two style references**

```bash
head -200 lecture_presentations/M1D2.html
sed -n '1,50p' syllabus/blockchain-syllabus.html
sed -n '275,350p' syllabus/blockchain-syllabus.html
```

Note from M1D2.html: the colour variables (`--bg`, `--cyan`, `--yellow`), the font imports (IBM Plex Mono, IBM Plex Sans, Space Grotesk), and the dark surface palette.

Note from blockchain-syllabus.html: the JavaScript pattern that renders modules as tabs, then renders the active module's days as expandable cards. The data shape is `syllabus = [{module, title, color, weeks, days: [{day, title, topics:[...], exercise}]}]`.

- [ ] **Step 2: Create `syllabus/COURSE_PLAN.html`** with the structure below.

The file MUST contain:

1. **`<head>`** — title "Faculty of Polytechnic — Python in 8 Weeks", IBM Plex font imports (same as M1D2.html), inline CSS matching the dark palette from M1D2.html (`:root` block with `--bg`, `--surface`, `--card`, `--cyan`, `--yellow`, `--green`, `--purple`, etc.).

2. **`<header>`** — eyebrow "Course Plan · v1 · 2026-05-29", title "Python in 8 Weeks", sub "A 2-month introduction for diploma CS students".

3. **Stats row** (4 stat boxes): `3 Modules` · `40 Days` · `5 Mini-Projects` · `1 Capstone`.

4. **"How it works" section** — three columns:
   - **Daily rhythm:** 09:00–10:15 Lecture · 11:00–12:00 Lab
   - **Submission flow:** Fork → Personal folder → PR
   - **Assessment:** 5 Friday projects · 3 mini-quizzes · final mini-test · capstone

5. **Module tab bar** — 3 buttons: `M1 · Python Foundations`, `M2 · Python in Practice`, `M3 · Capstone: Tiny Blockchain`. Active tab shows a coloured underline (cyan for M1, purple for M2, yellow for M3).

6. **Active module's days** — rendered as expandable day cards. Each card shows: `Day NN · Title · Lab project`. Click to expand and show the "topics" list and the day's lab description. Use the same JS pattern as blockchain-syllabus.html (vanilla JS, no framework).

7. **Footer:** "Built for diploma CS students · 2026 · See `syllabus/COURSE_DESIGN.md` for the full design doc."

8. **The data** — embed the 40-day plan from `syllabus/COURSE_DESIGN.md` Section 4 into a `const syllabus = [...]` JavaScript array. The shape for each module must be exactly:

```js
{
  module: 1,
  title: "Python Foundations",
  color: "#00D4FF",
  weeks: "Weeks 1–3",
  days: [
    { day: 1,  title: "Binary + GitHub + PR flow",         topics: ["Bits and bytes", "GitHub account creation", "The browser-based PR flow"], lab: "problem_1.py — seconds in a week", done: true },
    { day: 2,  title: "Python Essentials I",                topics: ["Variables and types", "if/elif/else", "for and while loops", "Functions"], lab: "FizzBuzz + warm-ups", done: true },
    { day: 3,  title: "Collections",                       topics: ["Lists, tuples, dicts, sets", "Iteration patterns"], lab: "Review with class", done: true },
    { day: 4,  title: "I/O, Types & Conversions",          topics: ["input() returns a string", "int() / float() / str()", "f-strings revisited", "Common conversion bugs"], lab: "Greeter + tip calculator" },
    { day: 5,  title: "Mini-project: About Me script",     topics: ["Recap", "Friday project"], lab: "Reads inputs, prints formatted bio. ★ input validation" },
    { day: 6,  title: "if/elif/else deep dive",            topics: ["Chained conditions", "Nested if", "Boolean operators"], lab: "Grade classifier, leap year check" },
    { day: 7,  title: "for loops + range()",               topics: ["Counters", "Accumulators"], lab: "Sum 1..N, multiplication tables" },
    { day: 8,  title: "while loops + break/continue",      topics: ["When to use which", "Infinite loop pitfall"], lab: "Find-first-match problems" },
    { day: 9,  title: "Combine day — loops + conditions",  topics: ["Pattern printing", "Prime check"], lab: "Combined exercises" },
    { day: 10, title: "Mini-Quiz 1 + Number Guessing Game",topics: ["15-min quiz", "Friday project"], lab: "Number Guessing Game. ★ track attempts, warmer/colder hint" },
    { day: 11, title: "Functions I",                       topics: ["Define, call", "Parameters", "Return values"], lab: "Refactor D5 script into functions" },
    { day: 12, title: "Functions II",                      topics: ["Multiple params, defaults", "Returning multiple values"], lab: "Geometry helpers (area, perimeter)" },
    { day: 13, title: "Scope — local vs global",           topics: ["Local vs global", "Why globals are usually bad"], lab: "Bug-hunt exercise" },
    { day: 14, title: "Combine day — refactor",            topics: ["Refactor messy code into clean functions"], lab: "Given spaghetti code, clean it" },
    { day: 15, title: "Mini-project: Simple Calculator",   topics: ["Friday project"], lab: "Functions for +, −, ×, ÷, %. ★ history of operations" },
  ]
}
```

Repeat for module 2 (`color: "#A78BFA"`, `weeks: "Weeks 4–6"`, days 16–30) and module 3 (`color: "#FFD43B"`, `weeks: "Weeks 7–8"`, days 31–40), using the day-by-day content from `syllabus/COURSE_DESIGN.md` Section 4. Each day's `topics` array should be 2–4 short phrases, and `lab` should be the lab/project description.

The `done: true` flag should be present on days 1, 2, and 3 only. Render those cards with reduced opacity (0.6) and a "✓ done" badge in the corner.

- [ ] **Step 3: Verify the HTML is valid and self-contained**

Run: `python3 -c "import html.parser; p=html.parser.HTMLParser(); p.feed(open('syllabus/COURSE_PLAN.html').read()); print('OK')"`
Expected: `OK`.

Run: `grep -c 'syllabus = \[' syllabus/COURSE_PLAN.html`
Expected: `1`.

Run: `grep -c 'module: 1' syllabus/COURSE_PLAN.html`
Expected: `1`.

Run: `grep -c 'module: 2' syllabus/COURSE_PLAN.html`
Expected: `1`.

Run: `grep -c 'module: 3' syllabus/COURSE_PLAN.html`
Expected: `1`.

- [ ] **Step 4: Manual visual check**

Open `syllabus/COURSE_PLAN.html` in a browser. Verify:
- Header renders with the title and tagline
- Stats row shows 4 boxes
- Module tabs are clickable; clicking switches the displayed days
- Day cards expand on click to reveal topics
- Days 1, 2, 3 appear visually de-emphasised (opacity 0.6) with a "done" badge

- [ ] **Step 5: Commit**

```bash
git add syllabus/COURSE_PLAN.html
git commit -m "feat(syllabus): add interactive Python-in-8-weeks course overview page"
```

---

## Task 5: Build `lecture_presentations/M1D4.html` — Day 4 lecture deck

**Files:**
- Create: `lecture_presentations/M1D4.html`

The file MUST be a single self-contained HTML file that exactly matches the structure, CSS, JavaScript, HUD controls, and slide animation pattern of `lecture_presentations/M1D2.html`. Read M1D2.html fully before building.

- [ ] **Step 1: Re-read M1D2.html and M1D3.html to understand the deck pattern**

```bash
wc -l lecture_presentations/M1D2.html lecture_presentations/M1D3.html
sed -n '1,200p' lecture_presentations/M1D2.html
```

Note the structure: `<head>` with fonts + inline CSS · `<body>` containing `.progress`, `.scaler > .stage` wrapping all `<section class="slide">` blocks · `.hud` + `.hint` fixed elements · `<script>` at the bottom handling keyboard nav (Arrow keys, Space, Home/End), the slide counter, the progress bar.

- [ ] **Step 2: Create `lecture_presentations/M1D4.html`** with the following slide outline. Every slide is a `<section class="slide">`. The first active slide gets the `active` class.

**Title:** `Module 1 · Day 4 — I/O, Types & Conversions`

**Slides (12 total):**

1. **TITLE** — Eyebrow: "Module 1 · Day 4 · From Bits to Blockchain". Big title: "I/O, Types & Conversions". Subtitle: "Day 4 of a 40-day journey".

2. **AGENDA** — Title: "Today's roadmap". Five-step list:
   - `input()` — talking to the user
   - Why `"1" + "2"` is `"12"`
   - Type conversion — `int()`, `float()`, `str()`
   - f-strings revisited
   - Lab — Greeter + Tip Calculator

3. **HOOK** — Title: "Until today, your programs talked to themselves." Body: "Today, they start talking to *you*. Every real program eventually needs input from a human. Python gives you exactly one tool for that: `input()`." Add a small illustrative code block:
   ```python
   name = input("What is your name? ")
   print(f"Hello, {name}!")
   ```

4. **`input()` BASICS** — Title: "`input()` — the front door to your program". Body: "Takes an optional prompt string, shows it to the user, waits for them to type, returns whatever they typed when they press Enter." Code block:
   ```python
   age = input("Your age? ")
   print("You typed:", age)
   ```
   Sidebar callout: "`input()` *always* returns a **string**. Always. Even if the user types digits."

5. **THE STRING TRAP** — Title: "Why `"1" + "2"` is `"12"`, not 3". Two code blocks side-by-side:
   ```python
   # What you wrote:
   a = input("First number: ")
   b = input("Second number: ")
   print(a + b)
   # Input: 1, 2  →  Output: "12"
   ```
   ```python
   # What you meant:
   a = int(input("First number: "))
   b = int(input("Second number: "))
   print(a + b)
   # Input: 1, 2  →  Output: 3
   ```

6. **TYPE CONVERSION** — Title: "Three converters you'll use forever". Three cards:
   - `int("42")` → `42` — text to whole number
   - `float("3.14")` → `3.14` — text to decimal
   - `str(42)` → `"42"` — number back to text

7. **CONVERSION BUGS** — Title: "Five conversions that will explode in your face". Code block:
   ```python
   int("abc")      # ValueError — not a number
   int("12.5")     # ValueError — int() refuses decimals
   int("  42  ")   # OK — whitespace is fine
   float("12.5")   # 12.5
   int(float("12.5"))  # 12 — the "convert then convert" trick
   ```
   Sidebar callout: "When in doubt, `float()` first, then `int()` if you need a whole number."

8. **f-STRINGS REVISITED** — Title: "f-strings — the only formatting you should use". Code block:
   ```python
   name = "Aisha"
   age  = 19
   print(f"{name} is {age} years old.")
   # Aisha is 19 years old.

   # You can do math inside the braces:
   print(f"In 5 years, {name} will be {age + 5}.")

   # You can format numbers:
   pi = 3.14159
   print(f"Pi to 2 places: {pi:.2f}")
   # Pi to 2 places: 3.14
   ```

9. **PUTTING IT TOGETHER** — Title: "A complete tiny program". Single code block showing the canonical D4 mini-example end-to-end:
   ```python
   name = input("Your name? ")
   age  = int(input("Your age? "))
   years_to_30 = 30 - age
   print(f"Hi {name}! You'll be 30 in {years_to_30} years.")
   ```

10. **FIVE MISTAKES** — Title: "Five mistakes you'll make today" (mirroring M1D2's "Five mistakes" slide structure). Numbered list:
    1. Forgetting `int()` around `input()` when you want a number.
    2. Calling `int("12.5")` — use `float()` first.
    3. Mixing `+` with strings and numbers: `"You are " + 19` crashes.
    4. Using old `%`-formatting or `.format()` — just use f-strings.
    5. Trusting the user — they might type "twenty" when you wanted `20`.

11. **LAB PREVIEW** — Title: "Today's lab — Greeter + Tip Calculator". Two cards:
    - **Greeter:** Ask name + age, print a personalised line including how old they'll be next year.
    - **Tip Calculator:** Ask the bill amount and tip percentage, print the tip and the total.
    Sidebar: "Submit via your fork → `students/<your-username>/D04_greeter.py`. See `lab/module_1_foundations/D04_greeter/problem.md` for the full brief."

12. **WHAT YOU CAN NOW DO** — Title: "What you can now do" (mirroring M1D2's closing slide). Three-line list:
    - Read input from a user and convert it to the right type.
    - Format output cleanly with f-strings.
    - Catch and avoid the "string vs number" bug class.
    Bottom note: "Next: `if/elif/else` deep dive on Day 6."

The `<script>` at the bottom of the file must include the same slide navigation logic as M1D2.html (Arrow keys / Space / Home / End for slide changes, progress bar update, slide counter update). Copy it from M1D2.html and adapt only the total slide count if the script reads it dynamically.

- [ ] **Step 3: Verify the deck loads and has the expected slide count**

Run: `grep -c 'class="slide"' lecture_presentations/M1D4.html`
Expected: `12`.

Run: `grep -c 'class="slide active"' lecture_presentations/M1D4.html`
Expected: `1` (only the title slide is active by default).

Run: `python3 -c "import html.parser; p=html.parser.HTMLParser(); p.feed(open('lecture_presentations/M1D4.html').read()); print('OK')"`
Expected: `OK`.

- [ ] **Step 4: Manual visual check**

Open `lecture_presentations/M1D4.html` in a browser. Verify:
- Title slide renders with the dark background and cyan accents.
- Arrow keys advance through slides; the progress bar at the top fills.
- The HUD bottom-right shows `1 / 12`, `2 / 12`, etc.
- All code blocks render with the syntax highlighting classes (`.kw`, `.str`, `.num`, `.com`).
- No JavaScript console errors.

- [ ] **Step 5: Commit**

```bash
git add lecture_presentations/M1D4.html
git commit -m "feat(deck): add M1D4 lecture deck — I/O, types, conversions"
```

---

## Task 6: Build the Day 4 lab folder

**Files:**
- Create: `lab/module_1_foundations/D04_greeter/problem.md`
- Create: `lab/module_1_foundations/D04_greeter/starter.py`
- Create: `lab/module_1_foundations/D04_greeter/example_run.txt`

- [ ] **Step 1: Create `lab/module_1_foundations/D04_greeter/problem.md`** with this content:

```markdown
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
```

- [ ] **Step 2: Create `lab/module_1_foundations/D04_greeter/starter.py`** with this content:

```python
# D4 — Greeter + Tip Calculator
#
# Read the full brief in problem.md.
# Implement both functions below. Run the file to test.

def greet():
    # 1. Ask the user for their name with input("Your name? ")
    # 2. Ask the user for their age and convert it to an int
    # 3. Print: f"Hi {name}! Next year you will be {age + 1}."
    pass


def tip_calculator():
    # 1. Ask for the bill amount (float)
    # 2. Ask for the tip percentage (float)
    # 3. Compute the tip and the total
    # 4. Print both, formatted to 2 decimal places: f"{value:.2f}"
    pass


if __name__ == "__main__":
    greet()
    print()  # blank line between the two problems
    tip_calculator()
```

- [ ] **Step 3: Create `lab/module_1_foundations/D04_greeter/example_run.txt`** showing the expected interaction:

```
$ python3 D04_greeter.py
Your name? Aisha
Your age? 19
Hi Aisha! Next year you will be 20.

Bill amount? 850.50
Tip percentage? 12
Tip: 102.06
Total: 952.56
```

- [ ] **Step 4: Verify the starter file parses as valid Python**

Run: `python3 -m py_compile lab/module_1_foundations/D04_greeter/starter.py`
Expected: command exits 0, no output.

- [ ] **Step 5: Verify the example output math**

Sanity-check the tip math by hand: `850.50 × 0.12 = 102.06`. `850.50 + 102.06 = 952.56`. ✓ Matches `example_run.txt`.

- [ ] **Step 6: Commit**

```bash
git add lab/module_1_foundations/D04_greeter/
git commit -m "feat(lab): add D4 Greeter + Tip Calculator lab problem and starter"
```

---

## Task 7: Final end-to-end verification

This task does not create files. It verifies the whole scaffold works together
before declaring the plan complete.

- [ ] **Step 1: Verify directory layout matches the spec**

Run: `find . -path ./.git -prune -o -type d -print | grep -E "^\./(lab|students|quizzes|_dev|lecture_presentations|syllabus|docs)" | sort`

Expected output:
```
./_dev
./_dev/helpers
./_dev/samples
./docs
./docs/superpowers
./docs/superpowers/plans
./lab
./lab/module_1_foundations
./lab/module_1_foundations/D01_seconds_in_week
./lab/module_1_foundations/D04_greeter
./lab/module_2_practice
./lab/module_3_capstone
./lecture_presentations
./quizzes
./students
./syllabus
```

- [ ] **Step 2: Verify all required new files exist**

Run:
```bash
for f in \
  README.md \
  syllabus/COURSE_DESIGN.md \
  syllabus/COURSE_PLAN.html \
  lecture_presentations/M1D2.html \
  lecture_presentations/M1D3.html \
  lecture_presentations/M1D4.html \
  lab/module_1_foundations/D01_seconds_in_week/problem.md \
  lab/module_1_foundations/D01_seconds_in_week/starter.py \
  lab/module_1_foundations/D04_greeter/problem.md \
  lab/module_1_foundations/D04_greeter/starter.py \
  lab/module_1_foundations/D04_greeter/example_run.txt \
  problem_1.py \
  syllabus/blockchain-syllabus.html \
; do [ -f "$f" ] && echo "OK  $f" || echo "MISSING  $f"; done
```

Expected: every line starts with `OK`.

- [ ] **Step 3: Verify the deprecated and orphan files**

Run: `[ -f lab/problem_1.py ] && echo "STILL EXISTS (BUG)" || echo "deleted OK"`
Expected: `deleted OK`.

Run: `head -3 problem_1.py | grep -c SUPERSEDED`
Expected: `1`.

Run: `head -50 syllabus/blockchain-syllabus.html | grep -c DEPRECATED`
Expected: `1`.

- [ ] **Step 4: Open all HTML in a browser for visual review**

Open in a browser, in this order:
1. `syllabus/COURSE_PLAN.html` — verify tabs work, day cards expand, days 1–3 show as "done".
2. `lecture_presentations/M1D4.html` — verify all 12 slides navigate correctly with arrow keys, no console errors.
3. `syllabus/blockchain-syllabus.html` — verify the yellow deprecation banner is visible at the top.

- [ ] **Step 5: Verify git state is clean**

Run: `git status --porcelain`
Expected: empty output (everything committed).

Run: `git log --oneline -10`
Expected: the recent commits include (in reverse chronological order):
- `feat(lab): add D4 Greeter + Tip Calculator lab problem and starter`
- `feat(deck): add M1D4 lecture deck — I/O, types, conversions`
- `feat(syllabus): add interactive Python-in-8-weeks course overview page`
- `docs: rewrite README to describe the 8-week Python course and fork-based PR flow`
- `chore: mark legacy syllabus and Day 1 problem files as superseded`
- `scaffold: add new lab/students/quizzes/_dev directory structure and migrate D1`

- [ ] **Step 6: Push to remote (optional, faculty decision)**

This step is gated on the user's explicit instruction. If approved:

```bash
git push origin main
```

If not yet ready to push, leave the commits local and proceed.

---

## Out of scope (separate future plans)

The following items are intentionally NOT part of this plan:

- Days 5–40 lecture decks and lab folders. These will be built one week at a
  time, the weekend before each teaching week, as separate plans.
- The Mini-Quiz 1/2/3 and final mini-test content files. To be designed
  closer to the relevant dates (Wk 2, Wk 4, Wk 6, Wk 8).
- The `solutions/` branch and its content. To be initialised at the end of
  each week with reference solutions for that week's labs.
- Onboarding the student GitHub Team / org settings. Faculty action outside
  the repo.
- Verifying GitHub Codespaces is enabled on the org. Faculty action outside
  the repo (~1 min on github.com).
- Committing `syllabus/COURSE_DESIGN.md` itself — that's done in this plan's
  prerequisites (or under faculty's direct control if they prefer to commit
  it with a specific message).

## Prerequisite — commit the design doc

Before running Task 1, ensure `syllabus/COURSE_DESIGN.md` is committed:

```bash
git status syllabus/COURSE_DESIGN.md
# If untracked or modified:
git add syllabus/COURSE_DESIGN.md
git commit -m "docs(syllabus): add COURSE_DESIGN spec for the 8-week Python course"
```
