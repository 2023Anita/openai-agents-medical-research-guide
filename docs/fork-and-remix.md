# Fork and Remix Guide

This repository is meant to be copied, rewritten, and published as a new course. The goal is not to clone the medical research assistant forever. The goal is to learn the pattern and turn it into your own interactive course lab.

## The remix pattern

Use this loop:

```text
Choose a real audience
→ pick one concrete project
→ keep the course short
→ add static checkpoints
→ include runnable code
→ publish with GitHub Pages
```

The original course teaches the OpenAI Agents SDK through a medical research assistant. Your fork can teach another domain with the same structure.

## Remix examples

| Direction | New project idea | What to replace |
| --- | --- | --- |
| Nursing research | Nursing research assistant | Replace ICU examples with nursing scales, care-quality outcomes, and nursing manuscript tasks. |
| Pharmacy research | Medication safety research assistant | Replace study examples with pharmacovigilance, adverse event coding, and drug safety literature planning. |
| Public health | Community health research assistant | Replace examples with surveillance, exposure/outcome definitions, and population-level ethics. |
| AI education | Prompt-to-agent course lab | Replace medical research with a general agent-building workflow and software project exercises. |

## 30-minute fork checklist

1. Fork the repository on GitHub.
2. Clone your fork locally.
3. Run:

```bash
npm install
npm run dev
```

4. Update the public identity:
   - `README.md`
   - `src/pages/index.astro`
   - `src/assets/brand/logo.png`
   - `src/assets/brand/banner.png`
   - `public/og-image.png`

5. Update the course content:
   - keep the three-language folder structure if you want multilingual publishing
   - start with one language if you want a smaller fork
   - keep the chapter slug pattern so links stay predictable

6. Update the interactive checkpoints:
   - each chapter imports `InteractiveExercise`
   - each checkpoint should test a concrete decision
   - avoid questions that need private data or clinical judgment

7. Run:

```bash
npm run build
```

8. Publish with GitHub Pages.

## What to keep

Keep these ideas even if you change the topic:

- one real project as the learning spine
- one short checkpoint per chapter
- one open practice task per chapter
- a clear safety or scope boundary
- screenshots in the README
- a path for learners to fork and publish their own version

## What to rewrite

Rewrite these areas for your own course:

- the audience
- the example project
- the chapter scenarios
- the checkpoint questions
- the demo code
- the safety boundary
- the README positioning

## Safety reminder

If your fork involves medicine, finance, law, education records, or personal data, add a clear boundary. A course project should teach workflows and reasoning. It should not pretend to be a production decision system.
