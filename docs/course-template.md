# GitHub-Native Interactive Course Template

This template turns a fast-moving technology into a small, forkable course lab.

## One-sentence positioning

```text
This course teaches [technology] through one focused project: [project], for [audience], with [safety/scope boundary].
```

Example:

```text
This course teaches the OpenAI Agents SDK through one focused project: a medical research assistant, for doctors and AI builders, with a strict research-only safety boundary.
```

## Course structure

Use 6 to 8 chapters. Each chapter should follow the same rhythm:

1. One-sentence explanation
2. Plain-language analogy
3. Minimal code
4. Real domain scenario
5. Common mistakes
6. Interactive checkpoint
7. Open practice task

## Chapter template

````mdx
---
title: Chapter title
description: One short value statement.
sidebar:
  order: 1
---

import InteractiveExercise from '../../../../components/InteractiveExercise.astro';

## One-sentence explanation

Explain the concept in one short paragraph.

## Analogy

Use one concrete analogy that matches the audience.

## Minimal code

```python
# Keep this short enough to read in one screen.
```

## Real scenario

Show where this concept appears in the project.

## Common mistakes

- Mistake 1.
- Mistake 2.
- Mistake 3.

## Exercise

<InteractiveExercise
  id={"en-topic-chapter-check"}
  kind={"single"}
  title={"Decision checkpoint"}
  prompt={"Which option best matches the concept?"}
  options={[
    { "id": "a", "label": "Wrong but plausible option." },
    { "id": "b", "label": "Correct option." }
  ]}
  answers={["b"]}
  feedback={{
    "correct": "Correct. Explain why.",
    "incorrect": "Try again. Give a coaching hint.",
    "required": "Choose an answer before checking.",
    "completed": "Correct. Explain why."
  }}
  checkLabel={"Check answer"}
  resetLabel={"Try again"}
  completedLabel={"Completed"}
  typeLabel={"Single choice"}
  reviewNote={"This is a learning exercise. Real projects still need human review."}
  openPractice={"Open practice: change the example for your own project."}
/>
````

## Checkpoint design rules

- Test one decision at a time.
- Prefer realistic wrong answers over silly wrong answers.
- Explain the reason, not just the answer.
- Keep sensitive data out of questions and feedback.
- Use multiple choice when several conditions must all be true.

## README template

Your README should answer these questions in the first screen:

- What is this?
- Who is it for?
- How can I try it?
- How can I fork it?
- What is out of scope?

Use this order:

1. Title and one-sentence promise
2. Banner image
3. Live course, demo, and fork links
4. Screenshots
5. What makes this different
6. Quick start
7. Safety or scope boundary

## Publish checklist

```bash
npm install
npm run build
```

Then publish with GitHub Pages and verify:

- homepage opens
- docs pages open
- interactive checkpoint works
- screenshots render in README
- safety or scope boundary is visible
