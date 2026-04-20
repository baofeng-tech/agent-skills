# agentskill.sh Release

GitHub-ready release layer generated from `targetSkills/` for agentskill.sh import.

## Purpose

- Produce a root-level public skill repository that agentskill.sh can scan with `Analyze & Import`.
- Keep the frontmatter close to the open Agent Skills spec while making the repo shape explicit for GitHub import.
- Emit per-skill ZIP artifacts for direct-URL or manual update workflows.

## Recommended Submit Flow

1. Push this directory to the public GitHub repository root at `https://github.com/baofeng-tech/agent-skills`.
2. Open `https://agentskill.sh/submit`.
3. Paste the GitHub repo URL and run `Analyze & Import`.
4. Optionally add the GitHub webhook `https://agentskill.sh/api/webhooks/github` for faster sync.
5. Keep `index.json`, `index.md`, and `well-known-skills-index.json` at repo root for cleaner crawler discovery.

## Generated Skills

- `aisa-multi-search-engine`
- `aisa-provider`
- `aisa-tavily`
- `aisa-twitter-api`
- `aisa-twitter-command-center`
- `aisa-twitter-engagement-suite`
- `aisa-twitter-post-engage`
- `aisa-youtube-search`
- `aisa-youtube-serp-scout`
- `cn-llm`
- `last30days`
- `last30days-zh`
- `llm-router`
- `market`
- `marketpulse`
- `media-gen`
- `multi-search`
- `openclaw-aisa-youtube-aisa`
- `openclaw-media-gen`
- `openclaw-search`
- `openclaw-twitter`
- `openclaw-twitter-post-engage`
- `openclaw-youtube`
- `perplexity-research`
- `perplexity-search`
- `prediction-market`
- `prediction-market-arbitrage`
- `prediction-market-arbitrage-api`
- `prediction-market-arbitrage-zh`
- `prediction-market-data`
- `prediction-market-data-zh`
- `scholar-search`
- `search`
- `smart-search`
- `stock-analysis`
- `stock-dividend`
- `stock-hot`
- `stock-portfolio`
- `stock-rumors`
- `stock-watchlist`
- `tavily-extract`
- `tavily-search`
- `twitter`
- `twitter-autopilot`
- `twitter-command-center-search-post`
- `twitter-command-center-search-post-interact`
- `us-stock-analyst`
- `web-search`
- `x-intelligence-automation`
- `youtube`
- `youtube-search`
