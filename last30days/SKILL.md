---
name: last30days
description: 'Research the last 30 days across Reddit, X/Twitter, YouTube, TikTok, Instagram, Hacker News, Polymarket, and web search. Use when: the user needs recent multi-source research across the last 30 days.'
license: MIT
compatibility: Designed for Agent Skills compatible clients such as OpenClaw, Claude Code, Hermes, and GitHub-backed skill catalogs. Requires system binaries python3, bash, environment variables AISA_API_KEY and internet access to api.aisa.one.
metadata:
  author: AIsa
  version: 1.0.0
  homepage: https://aisa.one
  repository: https://github.com/baofeng-tech/agent-skills
  tags: twitter,x,youtube,search,research,market
  platforms: agentskills.io,agentskill.sh,github
  primary_env: AISA_API_KEY
allowed-tools: Read Bash Grep
---

# last30days

Research recent evidence across social platforms, community forums, prediction markets, and grounded web results, then merge everything into one brief.

## When to use

- Use when you need a last-30-days research brief on a person, company, product, market, tool, or trend.
- Use when you want a recent competitor comparison, launch reaction summary, creator/community sentiment scan, or shipping update.
- Use when you want structured JSON with `query_plan`, `ranked_candidates`, `clusters`, and `items_by_source`.

## When NOT to use

- Do not use for timeless encyclopedia questions with no recent evidence requirement.
- Do not use when you need only one official source and do not want social/community signals.

## Capabilities

- AISA-hosted planning, reranking, synthesis, grounded web search, X/Twitter search, YouTube search, and Polymarket search.
- Public Reddit and Hacker News retrieval with fail-soft behavior.
- Hosted discovery for TikTok, Instagram, Threads, and Pinterest when enabled in runtime config.
- Public publish bundles intentionally focus on the stateless research CLI and exclude the older watchlist / briefing / second-credential GitHub add-ons.

## Setup

- `AISA_API_KEY` is the only hosted credential used by the public skill surface.
- Python `3.12+` is required.
- Use repo-relative `scripts/` paths so the same skill layout works across compatible runtimes.
- Repo-local config can live at `./.last30days-data/config.env`, or you can pass `--api-key` directly.

## Quick Reference

```bash
bash scripts/run-last30days.sh "$ARGUMENTS" --emit=compact
python3 scripts/last30days.py "$ARGUMENTS" --api-key="$AISA_API_KEY"
python3 scripts/last30days.py "$ARGUMENTS" --emit=json
python3 scripts/last30days.py "$ARGUMENTS" --quick
python3 scripts/last30days.py "$ARGUMENTS" --deep
python3 scripts/last30days.py "$ARGUMENTS" --search=reddit,x,grounding
python3 scripts/last30days.py --diagnose
```

## Inputs And Outputs

- Input: a topic or comparison query such as `OpenAI Agents SDK`, `OpenClaw vs Codex`, or `Peter Steinberger`.
- Output: synthesized research plus `provider_runtime`, `query_plan`, `ranked_candidates`, `clusters`, and `items_by_source`.

## Example Queries

- `last30days OpenAI Agents SDK`
- `last30days Peter Steinberger`
- `last30days OpenClaw vs Codex`
- `last30days Kanye West --quick`
