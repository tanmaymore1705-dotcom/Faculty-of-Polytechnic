# GitHub Profile — Mini Capstone

**Module:** 1 Mini-Capstone · **Time budget:** 90 min · **Deliverable:** a live GitHub profile page

---

## What you are building

GitHub lets you create a **special repository** whose name exactly matches your username. The `README.md` inside that repo becomes your **public profile page** — anyone who visits your GitHub account sees it front and centre.

In this mini-capstone you will:

1. Create that special repo on GitHub.
2. Write a polished `README.md` in Markdown.
3. Turn it into a **website** you can share, hosted for free on GitHub Pages.

No Python required — this capstone is about Markdown, GitHub, and presenting yourself as a developer.

---

## Part 1 — Create your profile repository

1. Log in to [github.com](https://github.com).
2. Click **+** → **New repository**.
3. Set the **Repository name** to your **exact GitHub username** (e.g. if your username is `priya123`, the repo name must also be `priya123`).
4. Tick **Public**.
5. Tick **Add a README file**.
6. Click **Create repository**.

GitHub will show a green banner: *"✨ `username` is a special repository."* That confirms you did it correctly.

---

## Part 2 — Write your `README.md`

A ready-to-use starting point is provided in `template.md` (same folder as this file). Copy its contents into your repo's `README.md` and replace the placeholder text with your own details — every line marked with `...` or `Here` needs to be filled in.

Your `README.md` must include **all six sections** below. Use Markdown for every element — no plain paragraphs without any formatting.

### Required sections

#### 1. Header — your name and a one-line tagline

Use a level-1 heading for your name and a level-2 or blockquote for your tagline.

```markdown
# Priya Deshmukh
### Aspiring software developer | Polytechnic student | Python enthusiast
```

#### 2. About me

A short paragraph (3–5 sentences) introducing who you are: your course, your college, what you enjoy building, and one fun fact about yourself.

#### 3. Skills

A Markdown table listing the tools and technologies you have learned so far.

| Skill        | Level          |
|--------------|----------------|
| Python       | Beginner       |
| Git & GitHub | Beginner       |
| Markdown     | Intermediate   |

Add any other skills you genuinely have (e.g. MS Excel, HTML, a spoken language).

#### 4. Current projects

A bullet list with at least **two items** — one should be `Grade Buddy` (the capstone you built in this module). For each, write one sentence describing what it does.

```markdown
- **Grade Buddy** — a command-line app that tracks test scores and generates a report card.
- **GitHub Profile** — this very page, my first Markdown website.
```

#### 5. Goals

Two or three bullet points describing what you want to learn or build next (be specific — "learn Python file I/O" beats "get better at coding").

#### 6. Contact / find me

At least one working link using Markdown link syntax:

```markdown
[LinkedIn](https://linkedin.com/in/your-handle) · [Email](mailto:you@example.com)
```

---

## Part 3 — Host it as a website with GitHub Pages

1. In your profile repo, go to **Settings → Pages**.
2. Under **Source**, choose **Deploy from a branch**.
3. Select branch `main` and folder `/ (root)`, then click **Save**.
4. Wait about 60 seconds, then visit:
   `https://<your-username>.github.io/<your-username>/`

Your `README.md` is now a live website.

> **Tip:** GitHub Pages converts Markdown to HTML automatically. You do not need to write any HTML.

---

## Checklist before submitting

- [ ] Repo name exactly matches your GitHub username.
- [ ] Repo is **Public**.
- [ ] `README.md` contains all six required sections.
- [ ] At least one Markdown table and one Markdown link are present.
- [ ] GitHub Pages is enabled and the site loads at the URL above.

---

## How to submit

1. Paste the **link to your profile repo** and your **live GitHub Pages URL** as a comment on the class PR thread, or in the submission form your instructor shares.
2. Open a PR against upstream `Faculty-of-Polytechnic` `main` adding a file at:
   `students/<your-github-username>/github_profile_url.txt`
   containing just your two URLs (repo URL on line 1, Pages URL on line 2).

---

## Marking guide

| Criterion                                   | Marks |
|---------------------------------------------|-------|
| Repo created with correct username           | 10    |
| All six sections present                     | 30    |
| At least one table and one link              | 20    |
| Proper Markdown formatting throughout        | 20    |
| GitHub Pages site live and loading correctly | 20    |
| **Total**                                    | **100** |

---

## ★ Stretch challenges (optional)

- Add a **GitHub Stats card** using [github-readme-stats](https://github.com/anuraghazra/github-readme-stats) — it auto-updates with your activity.
- Add **badges** for languages or tools using [shields.io](https://shields.io).
- Add a custom **theme** to your Pages site by creating a `_config.yml` with `theme: minima` (or any [supported Jekyll theme](https://pages.github.com/themes/)).
- Write your About Me section in both **English and your regional language** side-by-side using a Markdown table.
