# Figma Design Spec

## Objective

Create a premium documentation design for `OpenAI Agents SDK for Medical Research`, a multilingual course for doctors, researchers, and AI builders.

The design should feel professional, calm, and credible. It should not feel like a startup landing page with loud gradients. The subject is medical research education, so clarity and trust matter more than spectacle.

## Frames

### 1. Home Desktop

- Size: 1440 × 1200.
- Header: brand text on the left, language switcher on the right.
- Hero:
  - Eyebrow: `Multilingual course · Python · Safety-first agents`
  - H1: `Build medical research agents with clarity, boundaries, and taste.`
  - Supporting copy: one paragraph explaining the medical research assistant project.
  - CTA buttons: `Start learning`, `View demo code`.
- Three cards:
  - `Agent Workflow`
  - `Medical Research Safety`
  - `Seamless Languages`
- Course map section:
  - Seven core chapters plus overview.

### 2. Home Mobile

- Size: 390 × 1200.
- Header stacks language switcher below brand.
- Hero H1 wraps cleanly, no text clipping.
- Cards become one column.
- Course map remains scan-friendly.

### 3. Docs Page

- Size: 1440 × 1200.
- Left sidebar with Course navigation.
- Main content width: 720-820 px.
- Right table of contents.
- Components:
  - Title block.
  - Hero image.
  - Callout for medical safety boundary.
  - Python code block.
  - Common mistakes list.
  - Exercise block.
  - Interactive checkpoint card with answer options and feedback states.

### 4. Language Switch State

- Show language menu with:
  - 中文
  - English
  - 日本語
- The selected language should be visible but restrained.
- Switching should imply same chapter, different language.

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

### Typography

- Primary font: Inter or system sans.
- Mono font: SF Mono or equivalent.
- Letter spacing: 0.
- Hero scale only on homepage; docs pages should use tighter professional type.

### Component Rules

- Cards: 8 px radius max.
- Buttons: pill shape is allowed only for clear CTA and language chips.
- Code blocks: dark, low-saturation, readable.
- Callouts: use teal accent, avoid alert-heavy red unless discussing risk.
- No decorative orbs or one-note purple gradients.

## Content Components

- Course card:
  - Small number.
  - Short title.
  - One concise explanatory paragraph.
- Safety callout:
  - Title: `Research only, not clinical advice`
  - Body: diagnosis, treatment, triage, medication, and patient-specific advice are out of scope.
- Exercise block:
  - Short task.
  - Expected output.
  - Human review reminder when relevant.
- Interactive checkpoint:
  - State 1, unanswered: neutral card, visible answer options, primary `Check answer` button.
  - State 2, correct: teal success feedback, completion chip visible, option layout unchanged.
  - State 3, incorrect: warm amber feedback with a coaching hint, no harsh error styling.
  - State 4, completed: restored completion state after refresh, no user answer text stored.
  - Supports single-choice and multiple-choice questions.
  - Includes an open practice prompt for forking or remixing the lesson.

## Implementation Notes

- The implemented site uses Astro Starlight.
- CSS tokens live in `src/styles/custom.css`.
- Landing page lives in `src/pages/index.astro`.
- Documentation pages live under `src/content/docs/{zh,en,ja}/`.
- Interactive checkpoint component lives in `src/components/InteractiveExercise.astro`.
- Checkpoint state is static and browser-local; no backend, login, database, or API key is required.
