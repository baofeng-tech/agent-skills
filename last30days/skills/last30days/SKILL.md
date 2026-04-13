---
name: last30days-v3-spec
version: "1.0.0"
description: "Internal runtime spec for the AISA-first last30days pipeline."
argument-hint: "last30days codex vs claude code"
allowed-tools: Bash, Read, Write, WebSearch
homepage: https://github.com/mvanhorn/last30days-skill
repository: https://github.com/mvanhorn/last30days-skill
author: mvanhorn
license: MIT
user-invocable: false
---

# last30days internal spec

Use `last30days` when the user wants recent, cross-source evidence from roughly the last 30 days.

## Runtime contract

1. Plan the query.
2. Retrieve per `(subquery, source)`.
3. Normalize and dedupe.
4. Extract best snippets.
5. Fuse with weighted RRF.
6. Rerank.
7. Cluster evidence.
8. Render a single brief.

## Local development entrypoints

- `bash scripts/run-last30days.sh ...`
- `bash scripts/run-tests.sh`
- `bash scripts/run-watchlist.sh ...`
- `bash scripts/run-briefing.sh ...`
- `bash scripts/run-evaluate.sh ...`
- `bash scripts/dev-python.sh` resolves the preferred Python 3.12+ interpreter

## Environment

- Python 3.12+ is required.
- `AISA_API_KEY` is the default hosted credential.
- Public/official sources remain available without AISA where supported:
  - Reddit public JSON
  - Hacker News Algolia
  - GitHub official/public access
  - Polymarket public data when hosted proxy is absent

## Source policy

- Prefer AISA for X, YouTube, web grounding, Polymarket, and LLM calls.
- Keep `reddit`, `tiktok`, `instagram`, `threads`, and `pinterest` in the source model.
- Treat legacy third-party integrations as compatibility fallbacks, not as the recommended default path.

## Output model

- `compact` and `md`: cluster-first markdown
- `json`: full v3 report
- `context`: short synthesis-oriented context

Important report fields:

- `provider_runtime`
- `query_plan`
- `ranked_candidates`
- `clusters`
- `items_by_source`
- `errors_by_source`
