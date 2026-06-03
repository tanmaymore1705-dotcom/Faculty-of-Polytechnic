# Faculty of Polytechnic — 2-Month Python Course

**Design doc · 2026-05-29 · v1**

This document is the active course plan. The previous `blockchain-syllabus.html`
(Bits → Polkadot/Smoldot in 40 days, JS/Rust) was scrapped as too advanced for
the audience and is kept in this folder only as historical reference.

---

## 1. Audience & Constraints

- **Students:** Diploma CS students, first-time programmers, **mixed skill spread**
  (a few sharp, many struggling).
- **Already taught by Day 3:**
  - Day 1: binary basics, GitHub account creation, browser-based PR flow (via `problem_1.py`)
  - Day 2: Python Essentials I — variables, types, `if/else`, loops, functions, FizzBuzz (`M1D2.html`)
  - Day 3: Collections — lists, tuples, dicts, sets (`M1D3.html`)
- **Schedule:** Mon–Fri × 8 weeks ≈ 40 working days
  - 9:00 – 10:15 (75 min) — lecture
  - 11:00 – 12:00 (60 min) — practical lab
- **Language:** Python only (no JS/Rust).
- **Slide format:** HTML files matching the style of `M1D2.html` / `M1D3.html`.
- **No formal external exam.** Faculty conducts mini-tests; portfolio is the
  body of PRs students produce.

## 2. Goal

By the end of the course, students should be:

1. Comfortable writing small Python programs from scratch (variables, control
   flow, functions, lists/dicts, files, error handling).
2. Familiar with the GitHub PR workflow as a daily habit.
3. Able to build a working "tiny blockchain" in Python that mirrors the
   structure of a real Polkadot block, with a simplified Proof-of-Work loop
   and a conceptual understanding of how Polkadot's Nominated Proof-of-Stake
   differs.

The blockchain finale is **a Python-first project** that happens to be about
blockchain — not a blockchain course that happens to use Python.

## 3. Structure — "Spiral" cadence

Each week has one theme that ends in a Friday mini-project.

| Day      | Role                                                       |
| -------- | ---------------------------------------------------------- |
| Mon–Wed  | Introduce + drill the week's concept in small bites (2 lab problems each) |
| Thu      | "Combine" day — one larger problem using everything Mon–Wed |
| Fri      | Short recap lecture + **mini-project lab** (PR is the weekly artifact) |

Every other Friday (Wk 2, 4, 6) starts with a **15-minute mini-quiz** before the
project. The final mini-test is on D39 (Wk 8 Thu).

Every lab includes one **★ stretch problem** — ungraded, optional, designed for
the strong students so they don't disengage. A student completing 10+ stretch
problems across the course earns a "Stretch Award" at the wrap-up.

## 4. The 8-week roadmap

### Module 1 — Python Foundations (Weeks 1–3, D1–D15)

| Day | Topic                                            | Lab                                       |
| --- | ------------------------------------------------ | ----------------------------------------- |
| D1  | Binary + GitHub + PR flow (done)                 | `problem_1.py` — seconds in a week        |
| D2  | Python Essentials I — vars, if/else, loops, funcs (done) | FizzBuzz + warm-ups               |
| D3  | Collections — lists, tuples, dicts, sets (done)  | (review with class)                       |
| D4  | I/O, types, conversions — `input()`, `int()`/`str()`, f-strings revisited | Greeter + tip calculator |
| D5 (Fri) | Recap + **Mini-project: "About Me" script** | Reads inputs, prints formatted bio. ★ input validation |
| D6  | `if/elif/else` deep dive — chained, nested, boolean ops | Grade classifier, leap year check |
| D7  | `for` loops + `range()` — counters, accumulators | Sum 1..N, multiplication tables           |
| D8  | `while` loops, `break`/`continue`, infinite loops | Find-first-match problems                |
| D9  | Combine day — loops + conditions                 | Pattern printing, prime check             |
| D10 (Fri) | **Mini-Quiz 1** + **Mini-project: Number Guessing Game** | ★ track attempts, warmer/colder hint |
| D11 | Functions — define, call, parameters, return     | Refactor D5 script into functions         |
| D12 | Multiple params, defaults, returning multiple values | Geometry helpers (area, perimeter)    |
| D13 | Scope — local vs global; why globals are usually bad | Bug-hunt exercise                     |
| D14 | Combine day — refactor messy code into clean functions | Given spaghetti code, clean it       |
| D15 (Fri) | **Mini-project: Simple Calculator**       | Functions for +, −, ×, ÷, %. ★ history of operations |

### Module 2 — Python in Practice (Weeks 4–6, D16–D30)

| Day | Topic                                            | Lab                                       |
| --- | ------------------------------------------------ | ----------------------------------------- |
| D16 | String methods — `split`, `join`, `replace`, `lower`, `strip` | Clean up messy text          |
| D17 | String slicing + indexing — `s[2:5]`, `s[::-1]`  | Palindrome check, initials extractor      |
| D18 | List operations — `append`, `sort`, `index`, membership | Roll-call manager                  |
| D19 | Combine day — text + list together               | Word-list deduplicator                    |
| D20 (Fri) | **Mini-Quiz 2** + **Mini-project: Word Counter** | Count words/lines/chars in a paragraph |
| D21 | Dict basics — key/value, lookup, iteration       | Build a tiny **wallet-address → owner** lookup (Polkadot flavor) |
| D22 | Common dict patterns — counting, grouping        | Vote tally, group names by first letter   |
| D23 | Sets — unique values, membership                 | Find common/unique items between lists    |
| D24 | Combine day — nested dicts/lists                 | Library catalog (book → author/year)      |
| D25 (Fri) | **Mini-project: Word Frequency Counter** | Read text → dict of word counts, top 5    |
| D26 | Reading text files — `open`, `with`, line iteration | Read a names file, print each          |
| D27 | Writing files; CSV-like data by hand (split on comma) | Save results to a file              |
| D28 | `try/except` basics — file-not-found, bad input  | Robust input handler                      |
| D29 | `import` — `random`, `math`, `datetime`. **Includes a "pick a validator weighted by stake" snippet** to seed D36. | Random quiz generator |
| D30 (Fri) | **Mini-Quiz 3** + **Mini-project: Grade Sheet Reader** | Read CSV of marks, compute avg & grade |

### Module 3 — Capstone: Tiny Blockchain in Python, Polkadot-Themed (Weeks 7–8, D31–D40)

Polkadot is the running real-world anchor throughout this module.

| Day | Topic + Polkadot anchor                                                  | Lab                                       |
| --- | ------------------------------------------------------------------------ | ----------------------------------------- |
| D31 | **What is a hash?** `hashlib.sha256`. Real-world: Polkadot block hashes use Blake2. Show a block on Subscan, point at the `hash` field. | Hash strings; observe avalanche effect |
| D32 | **A block = a dict.** Polkadot blocks have `parent_hash`, `number`, `state_root`, `extrinsics_root`. Our toy block mirrors the first two. | Write `make_block()` with those field names |
| D33 | **A chain = a list.** Every Polkadot block points to its parent via `parent_hash` — same idea, simpler form. Show two consecutive blocks on Subscan, prove the link. | Build a 3-block chain manually |
| D34 | **Validation.** Polkadot validators run a much heavier check (signatures, state transitions). Ours: "does each `parent_hash` match the previous block's `hash`?" | Tamper with one block, prove `is_valid_chain()` catches it |
| D35 (Fri) | **Capstone Checkpoint** — working linked + validated chain        | ★ add an `extrinsics` field (list of "transactions") |
| D36 | **Consensus.** Bitcoin uses Proof of Work — we code that, it's satisfying. **Polkadot uses Nominated Proof of Stake** — validators are *chosen by how much DOT is staked behind them*. End of lecture: a 20-line weighted-random "pick the next validator" simulation to compare. | Mine 3 blocks with simplified PoW. ★ rewrite as PoS validator picker |
| D37 | **CLI menu.** Frame as "your own mini Polkadot.js, but in the terminal." | Wrap chain ops in an `add/view/validate` menu |
| D38 | **Save/load JSON.** Real Polkadot nodes persist state in a database; we use a JSON file. | Persist chain across runs                |
| D39 | **Final mini-test** (60 min practical — 2 Python problems + 1 small blockchain extension) | — |
| D40 (Fri) | **Presentations + course wrap-up.** Last 30 min: "where to go next" — Polkadot docs, Subscan, substrate-connect, and the old `blockchain-syllabus.html` as their "next 6 months" reading list. | Each student demos their chain (~5 min) |

## 5. Assessment

### Mini-tests faculty conducts

| Test          | When           | Format                                              |
| ------------- | -------------- | --------------------------------------------------- |
| Mini-Quiz 1   | D10 (Fri Wk 2) | 15 min, 2 short problems (loops + conditions)        |
| Mini-Quiz 2   | D20 (Fri Wk 4) | 15 min, 2 problems (strings + lists)                |
| Mini-Quiz 3   | D30 (Fri Wk 6) | 15 min, 2 problems (dicts + files)                  |
| Final mini-test | D39          | 60 min practical — 2 Python problems + 1 blockchain |

### Continuous PR portfolio

- ~30 daily lab PRs (participation credit)
- 5 Friday mini-project PRs (graded for correctness + style)
- 1 capstone PR (weighted highest)

### Suggested internal grading weights (adjust freely)

| Component                | Weight |
| ------------------------ | -----: |
| Daily PR participation   |   20%  |
| 3 mini-quizzes (5% each) |   15%  |
| 5 Friday mini-projects (5% each) | 25% |
| Final mini-test          |   15%  |
| Capstone PR              |   25%  |

The grading is intentionally light. Diploma beginners drown in heavy grading.
The point is that students leave with a *visible GitHub portfolio* and the
muscle memory of writing Python daily.

## 6. Lab IDE & Submission Workflow

### IDE — GitHub Codespaces

Browser-based VS Code on a free GitHub-hosted VM.

- Auth is automatic — students are already signed into github.com. No PAT, no
  SSH. They open their fork → `Code` → `Codespaces` → `Create codespace`.
- Real VS Code in the browser — Python, terminal, debugger, integrated git
  panel (visual stage/commit/push).
- Free tier: 60 core-hours/month per student. Course needs ~20 sessions/month
  × ~1h = well within budget. Codespaces auto-suspend after 30 min idle.
- The PR workflow students already learned (browser editor on github.com)
  remains a valid fallback for any day Codespaces flakes.

**Fallback** if institution blocks Codespaces: Google Colab with manual
"Save a copy to GitHub". Functional but less ".py file" feeling.

**Faculty to verify before D4:** open a Codespace on this repo from their own
GitHub account to confirm the feature is enabled in the org.

### Submission workflow — Fork + personal folder

Each student forks the upstream repo and works inside a personal folder in
their fork.

**Why forks (not shared branches on upstream):**

- **No write-access management** — students self-serve via the Fork button.
- **Fork sync conflicts are essentially impossible** — students only ever
  *add* files inside `students/<username>/`. When upstream adds a new lab
  starter, the student clicks "Sync fork" and pulls it cleanly.
- **Each fork is the student's permanent portfolio** — survives the end of
  the course, transferable to a job hunt.
- **Review UX is unchanged** — the upstream `Pull Requests` tab shows every
  open PR from every fork in one list. Faculty reviews from one place.

**One-time setup, D4 (after repo redesign):**

1. Student clicks **Fork** on the upstream repo.
2. Creates `students/<their-username>/README.md` in their fork.
3. Opens a PR upstream — the "I'm enrolled" PR. Faculty merges.

**Per lab problem (daily):**

1. Student clicks "Sync fork" on github.com to pull today's new starter.
2. Opens Codespaces on **their fork** (browser editor on the fork also works).
3. Creates `students/<username>/D04_greeter.py`, copies starter, solves.
4. Commits + pushes to their fork.
5. Opens PR upstream.
6. Faculty reviews + merges.

**End state of the upstream repo (Day 40):**

- `lab/` — faculty-owned curriculum, untouched by students.
- `students/<username>/` — populated with ~30 files per student via merged PRs.
  Visible portfolio for every student, browsable on github.com.

**Volume check:** ~30 students × ~30 lab problems ≈ ~900 PRs over 8 weeks
≈ 15–20 PRs/day. Reviewable in the 10:15–11:00 break window with a light bar
(does it run? does the output roughly match?).

**Hidden problem with the *current* workflow (status quo on `problem_1.py`):**
all students edit the same shared file → only the first PR to merge "wins" →
later PRs conflict and the file's state becomes whoever merged last. This
doesn't scale. The fork-per-student model eliminates it entirely.

## 7. Proposed Repo Structure

Move from the current flat layout to:

```
Faculty-of-Polytechnic/
├── README.md                          ← updated: how the course works
├── COURSE_OUTLINE.md                  ← plain-English week-by-week (student-facing)
│
├── lecture_presentations/             ← all .html decks
│   ├── M1D2.html  (done)
│   ├── M1D3.html  (done)
│   ├── M1D4.html
│   └── ... through M3D40.html
│
├── lab/                               ← faculty-owned curriculum (read-only to students)
│   ├── module_1_foundations/
│   │   ├── D01_seconds_in_week/
│   │   │   ├── problem.md             ← what to solve
│   │   │   └── starter.py             ← template students copy into their own folder
│   │   ├── D04_greeter/
│   │   ├── D05_about_me/              ← Friday mini-project
│   │   └── ...
│   ├── module_2_practice/
│   └── module_3_capstone/
│
├── students/                          ← grows as student PRs merge from their forks
│   ├── <username_1>/
│   │   ├── README.md                  ← their enrollment PR (D4)
│   │   ├── D01_seconds_in_week.py
│   │   ├── D04_greeter.py
│   │   └── ...
│   └── <username_2>/
│
├── solutions/                         ← on a separate `solutions` branch (faculty-only)
│   └── ... (mirrors lab/ structure)
│
├── quizzes/
│   ├── quiz_1_D10.md
│   ├── quiz_2_D20.md
│   ├── quiz_3_D30.md
│   └── final_mini_test_D39.md
│
├── syllabus/
│   ├── COURSE_DESIGN.md               ← this document
│   ├── COURSE_PLAN.html               ← interactive course overview (to build, replaces blockchain-syllabus.html as active)
│   ├── blockchain-syllabus.html       ← kept as historical reference
│   └── program_structure_instructions.pdf
│
└── _dev/                              ← per global config preference
    ├── helpers/                       ← reusable helper scripts
    └── samples/                       ← example outputs, sample fixtures
```

Key decisions inside this layout:

1. **Each lab is a folder, not a single file** — `problem.md` (what to solve)
   + `starter.py` (template). Lets us include sample inputs/expected outputs.
2. **`solutions/` lives on a separate `solutions` branch** (or private mirror).
   Students cannot see answers on `main`.
3. **Old `problem_1.py` at repo root** stays put — students' PR history depends
   on it. Add a comment noting it's superseded by
   `lab/module_1_foundations/D01_seconds_in_week/`.

## 8. What to build first (after this design is approved)

In order:

1. **`syllabus/COURSE_PLAN.html`** — student-facing interactive course overview
   (style modeled on existing decks; replaces `blockchain-syllabus.html` as
   the active plan to show students). To demo to the class on D4 as the
   official new structure.
2. **Repo skeleton** — create `lab/module_1_foundations/`,
   `lab/module_2_practice/`, `lab/module_3_capstone/` and migrate the existing
   `problem_1.py` into `lab/module_1_foundations/D01_seconds_in_week/`.
3. **`README.md`** — short rewrite explaining the course and the workflow.
4. **D4 lecture deck (`M1D4.html`)** and D4 lab (`D04_greeter/`).
5. From there, build out one week of decks + labs at a time, **the weekend
   before each week** so we can adjust based on what's landing.

A separate implementation plan will sequence this work.
