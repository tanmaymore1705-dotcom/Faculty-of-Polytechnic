# Faculty of Polytechnic — Python → Blockchain → Polkadot Course

**Design doc · 2026-05-29 · v1 · Updated 2026-06-12**

This document is the active course plan. The previous `blockchain-syllabus.html`
(Bits → Polkadot/Smoldot in 40 days, JS/Rust) was scrapped as too advanced for
the audience and is kept in this folder only as historical reference.

**2026-06-12 update:** After completing the Python foundations and practice modules
(Days 1–20), the course pivots to Blockchain Basics (Module 3, Days 21–30) and
Polkadot Basics (Module 4, Days 31–40). All content remains Python-grounded and
beginner-appropriate — no JavaScript, no Rust.

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
3. Able to understand blockchain fundamentals — hashing, block structure,
   chain validation, Proof of Work, and Proof of Stake — and demonstrate
   them in Python.
4. Familiar with Polkadot at a conceptual level: relay chain, parachains,
   DOT token, NPoS, and the ecosystem — enough to navigate Subscan and
   Polkadot.js apps confidently.

The course moves Python → Blockchain → Polkadot as a single flowing narrative:
Python skills directly enable the blockchain project; the blockchain project
directly explains Polkadot.

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
| D4  | I/O, types, conversions — `input()`, `int()`/`str()`, f-strings revisited (done) | Greeter + tip calculator |
| D5 (Fri) | Recap + **Mini-project: "About Me" script** (done) | Reads inputs, prints formatted bio. ★ input validation |
| D6  | `if/elif/else` deep dive — chained, nested, boolean ops (done) | Grade classifier, leap year check |
| D7  | `for` loops + `range()` — counters, accumulators (done) | Sum 1..N, multiplication tables           |
| D8  | `while` loops, `break`/`continue`, infinite loops (done) | Find-first-match problems                |
| D9  | Combine day — loops + conditions (done)          | Pattern printing, prime check             |
| D10 (Fri) | **Mini-Quiz 1** + **Mini-project: Number Guessing Game** (done) | ★ track attempts, warmer/colder hint |
| D11 | Functions — define, call, parameters, return (done) | Refactor D5 script into functions         |
| D12 | Multiple params, defaults, returning multiple values | Geometry helpers (area, perimeter)    |
| D13 | Scope — local vs global; why globals are usually bad | Bug-hunt exercise                     |
| D14 | Combine day — refactor messy code into clean functions | Given spaghetti code, clean it       |
| D15 (Fri) | **Mini-project: Simple Calculator**       | Functions for +, −, ×, ÷, %. ★ history of operations |

### Module 2 — Python in Practice (Weeks 4–5, D16–D20)

Python practice condensed to the essential skills needed before the blockchain module.

| Day | Topic                                            | Lab                                       |
| --- | ------------------------------------------------ | ----------------------------------------- |
| D16 | String methods — `split`, `join`, `replace`, `lower`, `strip` | Clean up messy text          |
| D17 | String slicing + indexing — `s[2:5]`, `s[::-1]`  | Palindrome check, initials extractor      |
| D18 | List operations — `append`, `sort`, `index`, membership | Roll-call manager                  |
| D19 | Combine day — text + list together               | Word-list deduplicator                    |
| D20 (Fri) | **Mini-Quiz 2** + **Mini-project: Word Counter** | Count words/lines/chars in a paragraph |

> **Note (2026-06-12):** The original Module 2 continued through D30 (dicts,
> sets, files, try/except). Those topics are now taught *in context* within
> Module 3 — dicts appear when we build blocks, files appear when we save the
> chain, try/except appears in validation. This tightens the course and prevents
> content from feeling disconnected.

### Module 3 — Blockchain Basics in Python (Weeks 5–7, D21–D30)

All blockchain concepts are taught through Python. Every new Python tool
(dicts, hashlib, json, try/except) is introduced exactly when needed to
build the next part of the chain.

| Day | Topic                                                    | Lab                                                  |
| --- | -------------------------------------------------------- | ---------------------------------------------------- |
| D21 | **What is a blockchain?** The trust problem, distributed ledgers, immutability | Draw a ledger; represent it as a Python dict |
| D22 | **Hashing: the magic fingerprint.** `hashlib.sha256`, avalanche effect, one-way property | Hash strings; observe output change with one character |
| D23 | **Anatomy of a block.** Block = Python dict with `index`, `timestamp`, `data`, `hash`, `previous_hash`. Genesis block. | Write `make_block()`, print the first block |
| D24 | **Building the chain.** Linking via `previous_hash`; chain = list of blocks. Tamper and see it break. | Build a 3-block chain; connect each block |
| D25 | **Validating the chain.** `is_valid_chain()` — two checks: recalculate hash + verify link. | Tamper with block 2, prove validation fails |
| D26 | **Proof of Work.** Mining = finding a nonce so the hash starts with zeros. Difficulty controls hardness. | Mine 3 blocks; try increasing difficulty |
| D27 | **Proof of Stake.** PoW vs PoS trade-offs. NPoS (Polkadot). Weighted validator selection in Python. | Write `weighted_choice()`, run 10 validator elections |
| D28 | **Wallets and transactions.** Key pairs concept; transactions as Python dicts `{from, to, amount}`. Add to block data. | Create 3 transactions, pack into a block |
| D29 | **The complete picture.** Full tiny blockchain walkthrough; compare to real Polkadot block structure on Subscan. | Run the complete chain end-to-end; add 5 transactions |
| D30 (Fri) | **Mini-Quiz 3 + Mini-project: Tiny Blockchain** | Full chain with mine/validate/view functions. ★ JSON save/load |

### Module 4 — Polkadot Basics (Weeks 7–8, D31–D40)

Purely conceptual — no new Python. Students apply blockchain understanding
to make sense of a real production network. All anchored in live tools
(Subscan, Polkadot.js apps).

| Day | Topic                                                    | Lab                                                  |
| --- | -------------------------------------------------------- | ---------------------------------------------------- |
| D31 | **What is Polkadot?** The multi-chain vision, scalability trilemma, shared security | Explore polkadot.network; identify relay chain + 3 parachains |
| D32 | **The Relay Chain.** Polkadot's consensus hub; validators; GRANDPA finality; 6-second block time | Open Subscan, find latest relay chain block, read every field |
| D33 | **Parachains.** Parallel blockchains; free security from relay chain; real examples (Moonbeam, Astar, Acala) | Pick one parachain on parachains.info; find it on Subscan |
| D34 | **DOT Token.** Three jobs: staking, governance, bonding. OpenGov voting. | Open Polkadot.js apps → staking; find active validators |
| D35 | **NPoS deep dive.** Validators, nominators, election algorithm, rewards, slashing. | Find top validator on Polkadot.js; count its nominators |
| D36 | **Reading Subscan.** Block explorer walkthrough; extrinsics; reading a real transfer | Find 3 real transfers; note from/to/amount |
| D37 | **The Polkadot ecosystem.** DeFi (Acala, HydraDX), smart contracts (Moonbeam, Astar), infrastructure (Asset Hub) | Visit parachains.info; pick 5 parachains and describe them |
| D38 | **Polkadot's future.** Polkadot 2.0 — Agile Coretime. JAM (awareness only). Resources for next steps. | Read one page of wiki.polkadot.network; summarise 3 facts |
| D39 | **Final mini-test** (60 min — 2 Python/blockchain problems + 1 Polkadot concept question) | — |
| D40 (Fri) | **Presentations + course wrap-up.** Student demos; the full arc Python → Blockchain → Polkadot; next steps. | Each student demos their tiny blockchain (~5 min) |

## 5. Assessment

### Mini-tests faculty conducts

| Test          | When           | Format                                                           |
| ------------- | -------------- | ---------------------------------------------------------------- |
| Mini-Quiz 1   | D10 (Fri Wk 2) | 15 min, 2 short problems (loops + conditions)                     |
| Mini-Quiz 2   | D20 (Fri Wk 4) | 15 min, 2 problems (strings + lists)                             |
| Mini-Quiz 3   | D30 (Fri Wk 6) | 15 min, 2 problems (blockchain Python — hash + block building)   |
| Final mini-test | D39          | 60 min — 2 Python/blockchain problems + 1 Polkadot concept question |

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

## 8. Build status (as of 2026-06-12)

| Module | Lectures done | Labs done |
| ------ | ------------- | --------- |
| M1 Python Foundations (D1–D15) | M1D2–M1D15 ✓ | module_1_foundations/ ✓ |
| M2 Python in Practice (D16–D20) | M2D16–M2D20 ✓ | module_2_practice/ (D16–D20) ✓ |
| M3 Blockchain Basics (D21–D30) | M3D21–M3D30 ✓ | module_3_blockchain/ — TBD |
| M4 Polkadot Basics (D31–D40) | M4D31–M4D40 ✓ | module_4_polkadot/ — TBD |

Lecture decks for Modules 3 and 4 were generated on 2026-06-12. Lab problem
files for D21–D40 are the next build priority.

A separate implementation plan will sequence this work.
