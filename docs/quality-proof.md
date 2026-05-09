# Quality Proof

This document records the project signals that make the repository credible as a public AI education portfolio piece.

## Current quality bar

| Area | Proof |
| --- | --- |
| Course site | Astro Starlight documentation site published with GitHub Pages. |
| Multilingual structure | Matching Chinese, English, and Japanese course folders with the same chapter slugs. |
| Interactive learning | Static single-choice and multiple-choice checkpoints embedded in every chapter. |
| Privacy boundary | Exercise completion uses browser `localStorage`; no backend, login, database, or learner text storage. |
| Demo code | Offline demo runs without network access; live demo requires the OpenAI Agents SDK and an API key. |
| Medical safety | Research-only boundary appears in README, docs, demo code, exercises, and contribution guidance. |
| Remix path | Fork/remix guide and reusable course template help learners create their own version. |

## Build and deployment

Local verification command:

```bash
npm run build
```

GitHub Pages deployment:

```text
.github/workflows/deploy.yml
```

The workflow uses Node 22, installs with `npm ci`, builds the Astro site, uploads the static artifact, and deploys to GitHub Pages.

## Coverage checklist

- Homepage explains the interactive course lab concept.
- `/case-study/` explains the portfolio story.
- README links to the live course, case study, checkpoint, demo code, remix guide, and course template.
- Each language has the same eight-chapter structure.
- Each chapter has one objective interactive checkpoint.
- Open practice prompts remain separate from static judging.
- The site does not claim clinical decision support.

## Portfolio review questions

Use these questions before sharing the repository:

1. Can a first-time visitor understand the project in five seconds?
2. Can a learner try the course without an API key?
3. Can a builder find the demo code quickly?
4. Can an educator understand how to fork and remix the course?
5. Is the medical safety boundary visible before someone reaches the code?

## Out of scope

- AI-based grading.
- User accounts or course analytics.
- Patient data handling.
- Clinical diagnosis, treatment, triage, or medication recommendation.
- Production medical decision support.
