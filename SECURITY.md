# Security Policy

## Supported project scope

This repository is an educational project. It is not a clinical decision-support system and must not be used to provide diagnosis, treatment, triage, medication advice, or patient-specific recommendations.

## Reporting a vulnerability

Please report security concerns through a GitHub issue only if the report does not include secrets, credentials, private medical data, or patient identifiers.

For sensitive reports, contact the maintainer through the GitHub profile associated with this repository and avoid posting private details publicly.

## Do not include

- API keys or tokens
- patient names, medical record numbers, or identifiable health data
- private institutional data
- screenshots containing credentials or private records

## Relevant security areas

- accidental exposure of API keys in examples or docs
- unsafe medical claims that cross from research support into clinical advice
- interactive exercise behavior that stores more data than intended
- GitHub Pages or workflow configuration issues

## Current data model

The interactive exercises are static. They store only lightweight completion state in the learner's browser with `localStorage`. They do not send answers to a server and do not require login, a database, or an API key.
