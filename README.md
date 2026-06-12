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
| `students/<firstname-lastname>/` | **Each student's personal folder** — one file per lab, e.g. `D04_greeter.py` |
| `quizzes/` | The 3 biweekly mini-quizzes + final mini-test |
| `syllabus/COURSE_DESIGN.md` | The full course plan (design doc) |
| `syllabus/COURSE_PLAN.html` | Student-facing interactive course overview |
| `syllabus/blockchain-syllabus.html` | Historical reference (deprecated 2026-05-29) |

## How students submit work

The PR workflow is **fork + personal folder**:

1. **One-time setup:**
   - Click **Fork** at the top of this repo on github.com.
   - Inside your fork, create the folder `students/<your-firstname-lastname>/`
     (e.g. `students/shreya-deshmukh/`). This is your personal workspace for
     the whole course — you only do this once.

2. **For each lab problem:**
   - Click **"Sync fork"** on your fork's homepage to get today's new starter.
   - Open your fork in [GitHub Codespaces](https://github.com/features/codespaces)
     (`Code → Codespaces → Create codespace`) — this is a free in-browser VS
     Code with Python already installed.
   - Create a new file inside **your own folder**:
     `students/<your-firstname-lastname>/D{NN}_{slug}.py`
     (e.g. `students/shreya-deshmukh/D04_greeter.py`).
   - Copy the day's `starter.py` into it and solve the problem.
   - Commit + push from VS Code's Source Control panel.
   - Open a Pull Request against the upstream `main` branch.

3. Faculty reviews and merges your PR.

Over 8 weeks each student accumulates ~30 files in their personal folder —
a visible portfolio on their GitHub profile.

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

## 🏆 Hall of Fame

Recognising students who go above and beyond — clean code, sharp problem-solving,
helping classmates, and tackling the optional ★ stretch problems. Faculty adds
names here as the course runs.

[Tanuja Karpe](students/tanuja-karpe)

[Ayushka Mutadik](students/aayushka-mutdak/)