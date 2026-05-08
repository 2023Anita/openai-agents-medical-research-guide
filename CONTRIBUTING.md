# Contributing

Thank you for helping improve this interactive course lab.

This project teaches the OpenAI Agents SDK through a medical research assistant. Contributions should make the course clearer, safer, easier to remix, or easier to run.

## Good contributions

- clearer explanations for beginners
- safer medical research examples
- better Chinese, English, or Japanese translations
- improved interactive checkpoint questions
- bug fixes in the Astro/Starlight site
- small improvements to the Python demo
- screenshots, diagrams, or README clarity improvements

## Safety boundary

Do not add content that provides diagnosis, treatment, triage, medication advice, or patient-specific recommendations.

Medical examples should stay at the research-support level:

- study design
- literature planning
- statistical analysis drafts
- manuscript structure
- ethics, privacy, and human-review reminders

## Local development

```bash
npm install
npm run dev
npm run build
```

Run the offline Python demo:

```bash
python3 "examples/medical_research_agent_demo.py" --offline
```

## Pull request checklist

- The change keeps the medical research boundary intact.
- `npm run build` passes.
- New or changed links work.
- Interactive exercises still have clear correct and incorrect feedback.
- Screenshots or README changes render correctly on GitHub.

## Translation notes

The course uses matching slugs across languages:

```text
/zh/guides/guardrails/
/en/guides/guardrails/
/ja/guides/guardrails/
```

When changing one chapter, check whether the same concept should be updated in the other languages.
