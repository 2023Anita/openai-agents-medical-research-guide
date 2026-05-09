# Portfolio Design Spec

## Objective

Create a premium portfolio-grade presentation for `OpenAI Agents SDK for Medical Research`: a multilingual, GitHub-native, interactive course lab for learning the OpenAI Agents SDK through a safety-first medical research assistant.

The design should feel credible, calm, clinical, and highly intentional. It should communicate that this is not a slide deck or a loose tutorial. It is a reusable AI education product prototype that learners can answer, fork, remix, and publish.

## Portfolio Message

Primary message:

```text
Not a slide deck. A forkable interactive course lab for medical research agents.
```

Supporting message:

```text
Read the concept, answer the checkpoint, inspect the code, fork the repo, and rebuild the course for your own research or teaching context.
```

## Frames

### 1. GitHub README Hero

- Size: 1440 × 900.
- Purpose: show what the GitHub repository should communicate in the first five seconds.
- Include:
  - project banner
  - badge row
  - live course CTA
  - interactive checkpoint CTA
  - fork/remix CTA
  - three screenshot slots
- Visual style:
  - GitHub-friendly white background
  - restrained medical teal accents
  - strong hierarchy, no decorative clutter

### 2. Homepage

- Size: 1440 × 1200.
- Header:
  - brand on the left
  - language switcher on the right
- Hero:
  - Eyebrow: `Interactive Course Lab · Python · Safety-first agents`
  - H1: `Build medical research agents in a course you can answer, fork, and remix.`
  - Supporting copy: explain the GitHub-native course lab concept.
  - CTA buttons: `Start learning`, `Try an exercise`, `View demo code`.
- Product panel:
  - `Answer`
  - `Feedback`
  - `Remix`
- Course cards:
  - `Agent Workflow`
  - `Medical Research Safety`
  - `Seamless Languages`

### 3. Interactive Exercise Card

- Size: 900 × 760.
- Show four states:
  - unanswered
  - incorrect
  - correct
  - completed after refresh
- Include:
  - question type chip
  - completion chip
  - answer options
  - primary check button
  - reset button
  - feedback panel
  - review note
  - open practice prompt
- The card should feel like a serious learning checkpoint, not a quiz toy.

### 4. Fork / Remix Flow

- Size: 1440 × 900.
- Show the learner journey:

```text
Read
→ Answer
→ Run demo
→ Fork
→ Replace scenario
→ Publish
```

- Include three remix examples:
  - nursing research assistant
  - pharmacy research assistant
  - public health research assistant
- Visual style:
  - clean flow diagram
  - small code/repo cues
  - no brand logos except project-owned assets

### 5. Portfolio Case Study Page

- Size: 1440 × 1600.
- Purpose: communicate the project as a portfolio-grade AI education product case.
- Include:
  - top navigation with course and GitHub links
  - case-study hero: `From slides to GitHub-native interactive AI course labs.`
  - problem section: passive PPT is not enough for fast-moving AI frameworks
  - proof cards: `Interactive Learning`, `Forkable Course Lab`, `Safety-first Medical AI`
  - three visual proof sections using the new assets
  - final CTA band linking to course, demo code, and GitHub repo
- Visual style:
  - editorial case-study rhythm
  - large hero type only in the opening section
  - wide visual panels, never nested cards
  - restrained clinical palette

### 6. Portfolio Visual Asset Pack

- Assets:
  - `public/portfolio/case-study-cover.svg`
  - `public/portfolio/learning-loop.svg`
  - `public/portfolio/agent-architecture.svg`
  - `public/portfolio/fork-remix-flow.svg`
- Purpose:
  - README proof strip
  - case-study page visual sections
  - social sharing and project presentation screenshots
- Design requirements:
  - all text must remain readable at GitHub README width
  - no dependency on external images or private Figma files
  - diagrams should explain product judgment, not decorate the page

## Visual System

### Color

- Background: `#F7FAF9`
- Surface: `#FFFFFF`
- Ink: `#15211F`
- Muted text: `#536762`
- Medical teal: `#238676`
- Mint accent: `#57C9B5`
- Border: `rgba(21, 33, 31, 0.12)`
- Code background: `#101917`
- Warning feedback: restrained amber, not alert-red

### Typography

- Primary font: Inter or system sans.
- Mono font: SF Mono or equivalent.
- Letter spacing: `0`.
- Hero-scale type only on homepage and portfolio hero frames.
- Docs, cards, and exercise states use compact professional type.

### Component Rules

- Cards: 8 px radius max.
- Buttons: pill shape allowed only for CTAs, language chips, and exercise actions.
- Code blocks: dark, low-saturation, readable.
- Callouts: teal accent for research boundary; amber only for coaching feedback.
- Do not use decorative orbs, bokeh blobs, loud gradients, or one-note purple palettes.

## Content Components

- README screenshot strip:
  - homepage
  - interactive exercise
  - docs page
- Portfolio proof strip:
  - case-study cover
  - learning loop
  - agent architecture
  - fork/remix path
- Safety callout:
  - Title: `Research only, not clinical advice`
  - Body: diagnosis, treatment, triage, medication, and patient-specific advice are out of scope.
- Interactive checkpoint:
  - Single-choice and multiple-choice variants.
  - Correct and incorrect feedback states.
  - Browser-local completion state only.
  - Open practice prompt for fork/remix work.
- Fork/remix card:
  - audience
  - replacement scenario
  - safety boundary
  - publish path

## Implementation Notes

- Site framework: Astro Starlight.
- Landing page: `src/pages/index.astro`.
- Portfolio case-study page: `src/pages/case-study.astro`.
- Interactive component: `src/components/InteractiveExercise.astro`.
- Course content: `src/content/docs/{zh,en,ja}/`.
- Visual tokens: `src/styles/custom.css`.
- README screenshots: `docs/assets/portfolio/`.
- Portfolio visuals: `public/portfolio/`.
- No backend, login, database, or API key is required for interactive exercises.
