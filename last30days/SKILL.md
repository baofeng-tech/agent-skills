---
name: last30days
description: "AISA-first multi-source social research across Reddit, X/Twitter, YouTube, TikTok, Instagram, Hacker News, Polymarket, GitHub, and the web. Use when user asks about: trending topics, social sentiment, Reddit discussions, Twitter reactions, YouTube coverage, TikTok trends, market predictions, recent news research, cross-platform evidence gathering, or any topic requiring multi-source synthesis from the last 30 days."
license: MIT
---

# last30days

Research any topic across 9+ social and prediction-market sources, then synthesize findings into a single evidence-based brief. All data retrieval routes through AIsa API by default.

## Workflow

**Step 1 — Resolve Python 3.12+**

```bash
for py in /usr/local/python3.12/bin/python3.12 python3.14 python3.13 python3.12 python3; do
  command -v "$py" >/dev/null 2>&1 || continue
  "$py" -c 'import sys; raise SystemExit(0 if sys.version_info >= (3, 12) else 1)' || continue
  LAST30DAYS_PYTHON="$py"; break
done
[ -z "${LAST30DAYS_PYTHON:-}" ] && echo "ERROR: Python 3.12+ required." >&2 && exit 1
```

**Step 2 — Choose search mode**

| Scenario | Command |
|----------|---------|
| Quick lookup | `"$LAST30DAYS_PYTHON" "{baseDir}/scripts/last30days.py" "$TOPIC" --quick --emit=compact` |
| Standard research | `"$LAST30DAYS_PYTHON" "{baseDir}/scripts/last30days.py" "$TOPIC" --emit=compact` |
| Deep investigation | `"$LAST30DAYS_PYTHON" "{baseDir}/scripts/last30days.py" "$TOPIC" --deep --emit=compact` |
| Specific sources | `"$LAST30DAYS_PYTHON" "{baseDir}/scripts/last30days.py" "$TOPIC" --search=reddit,x,youtube --emit=compact` |
| JSON output | `"$LAST30DAYS_PYTHON" "{baseDir}/scripts/last30days.py" "$TOPIC" --emit=json` |

**Step 3 — Synthesize results**

Read the output and synthesize into a brief. Weight cross-source corroboration highest. Use concise attributions: `per @handle`, `per r/subreddit`, `per YouTube channel`.

## Available Sources

| Source | Via | Notes |
|--------|-----|-------|
| X/Twitter | AIsa | `--search=x` |
| Reddit | AIsa + public API | `--search=reddit` — add `--subreddits=sub1,sub2` for specific communities |
| YouTube | AIsa | `--search=youtube` |
| TikTok | AIsa | `--search=tiktok` |
| Instagram | AIsa | `--search=instagram` |
| Hacker News | Algolia (free) | `--search=hackernews` |
| Polymarket | AIsa | `--search=polymarket` |
| GitHub | GitHub API | `--search=github` — requires `GH_TOKEN` or `gh auth` |
| Web/Grounding | AIsa | `--search=grounding` |

## Additional Commands

```bash
# Diagnostics
"$LAST30DAYS_PYTHON" "{baseDir}/scripts/last30days.py" --diagnose

# Watchlist management
"$LAST30DAYS_PYTHON" "{baseDir}/scripts/watchlist.py" list
"$LAST30DAYS_PYTHON" "{baseDir}/scripts/watchlist.py" add "topic"
"$LAST30DAYS_PYTHON" "{baseDir}/scripts/watchlist.py" remove "topic"

# Briefing generation
"$LAST30DAYS_PYTHON" "{baseDir}/scripts/briefing.py" generate

# Search quality evaluation
"$LAST30DAYS_PYTHON" "{baseDir}/scripts/evaluate_search_quality.py" --quick --limit=5
```

## Setup

- **Required**: Set `AISA_API_KEY` environment variable. This is the only setup needed.
- **Optional**: `GH_TOKEN` for GitHub search, `BSKY_HANDLE`/`BSKY_APP_PASSWORD` for Bluesky, `TRUTHSOCIAL_TOKEN` for Truth Social.
- On first run, recommend only `AISA_API_KEY`. Do not recommend browser cookie scanning, device auth, Bird, xAI keys, or other legacy paths.

## Output Expectations

- Prefer synthesis over source-by-source summaries.
- Weight cross-source corroboration highest.
- Preserve the report schema: `provider_runtime`, `query_plan`, `ranked_candidates`, `clusters`, `items_by_source`.

## Security & Permissions

- Read-only data retrieval; no accounts are created or modified.
- All API calls route through `api.aisa.one` via HTTPS.
- `AISA_API_KEY` is read from environment at runtime, never written to disk.
