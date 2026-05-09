# Demo Code

This folder contains the runnable example for the course.

## Files

| File | Purpose |
| --- | --- |
| `medical_research_agent_demo.py` | Offline and live demo of the medical research assistant workflow. |
| `requirements.txt` | Python dependency list for the live OpenAI Agents SDK demo. |

## Run without an API key

Use the offline mode when you want to understand the architecture without network access:

```bash
python3 "examples/medical_research_agent_demo.py" --offline
```

Offline mode prints the same mental model used throughout the course:

```text
Agent -> Runner -> Tools -> Specialists -> Guardrails -> Sessions -> Tracing
```

## Run with the OpenAI Agents SDK

Use the live mode when you want to see the real SDK execute the workflow:

```bash
python3 -m venv ".venv"
source ".venv/bin/activate"
pip install -r "examples/requirements.txt"
export OPENAI_API_KEY="sk-..."
python3 "examples/medical_research_agent_demo.py" --live
```

## What the demo shows

- A main medical research assistant agent.
- Literature, statistics, and writing specialist agents exposed as tools.
- Local Python functions converted with `@function_tool`.
- Structured output for a research brief.
- A medical safety guardrail for patient-specific clinical requests.
- A session object for project context.
- A trace wrapper for inspecting the run.

## Safety boundary

The demo is for medical research education only. It must not be used for diagnosis, treatment, triage, medication advice, or patient-specific recommendations. Real outputs require human review by researchers, statisticians, ethics reviewers, and clinical experts.

## Remix ideas

To adapt this demo for your own course:

- Replace the medical research question.
- Replace the specialist agents.
- Replace the tools with domain-specific helper functions.
- Keep the safety boundary visible in code and docs.
- Keep an offline path so learners can understand the shape before using an API key.
