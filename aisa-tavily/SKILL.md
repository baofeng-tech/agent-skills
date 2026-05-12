---
name: aisa-tavily
description: 'Search the web and extract page content through AIsa''s Tavily-backed API relay. Use when: the user needs web search, source discovery, current-news lookup, or content extraction from a URL. Supports concise result sets, deeper research, and news-focused queries.'
compatibility: Designed for Agent Skills compatible clients such as OpenClaw, Claude Code, Hermes, and GitHub-backed skill catalogs. Requires system binaries node, environment variables AISA_API_KEY and internet access to api.aisa.one.
metadata:
  author: AIsa
  version: 1.0.0
  homepage: https://aisa.one
  repository: https://github.com/baofeng-tech/agent-skills
  tags: x,search,research,aisa
  platforms: agentskills.io,agentskill.sh,github
  primary_env: AISA_API_KEY
allowed-tools: Read Bash Grep
---

# AIsa Tavily Search

Search the web and extract page content through AIsa's Tavily API relay. This skill is suited to research, source discovery, current-events lookup, and fetching readable content from a specific URL.

## When to use

- When the user needs web search results for a topic, question, company, product, or event
- When the user wants source discovery before summarizing or comparing information
- When the user needs current-news lookup with recent-day filtering
- When the user provides a URL and wants the page content extracted for downstream analysis

## When NOT to use

- Do not use this skill for sites that require login, browser interaction, or private account access
- Do not use this skill as a direct social-posting, upload, or OAuth workflow; it performs search and URL extraction only
- Do not use this skill when there is no network access to `api.aisa.one`

## Quick Reference

| Task | Command |
| --- | --- |
| Search the web | `node scripts/search.mjs "query"` |
| Search with more results | `node scripts/search.mjs "query" -n 10` |
| Run deeper research | `node scripts/search.mjs "query" --deep` |
| Search news | `node scripts/search.mjs "query" --topic news` |
| Search recent news only | `node scripts/search.mjs "query" --topic news --days 7` |
| Extract content from a URL | `node scripts/extract.mjs "https://example.com/article"` |

## Capabilities

- Search the web through AIsa's Tavily-backed relay
- Return concise, relevant result sets for AI-agent workflows
- Run deeper research with `--deep` for broader coverage
- Focus on news search with `--topic news`
- Limit news lookback windows with `--days <n>`
- Extract readable page content from a public URL

## Search

```bash
node scripts/search.mjs "query"
node scripts/search.mjs "query" -n 10
node scripts/search.mjs "query" --deep
node scripts/search.mjs "query" --topic news
```

## Options

- `-n <count>`: Number of results (default: 5, max: 20)
- `--deep`: Use advanced search for deeper research (slower, more comprehensive)
- `--topic <topic>`: Search topic - `general` (default) or `news`
- `--days <n>`: For news topic, limit to last n days

## Extract content from URL

```bash
node scripts/extract.mjs "https://example.com/article"
```

## Setup

Requirements:
- `node`
- `AISA_API_KEY`
- Internet access with outbound requests to `api.aisa.one`

Auth and network notes:
- This skill requires `AISA_API_KEY` from https://marketplace.aisa.one
- Requests are relayed through AIsa's unified API gateway at `https://aisa.one` and `api.aisa.one`
- This skill does not use OAuth
- This skill does not upload media or files
- This skill may send user search queries and public target URLs to the remote AIsa relay in order to return search results or extracted content

## Example Requests

- "Search for recent coverage of OpenAI enterprise pricing"
- "Find sources comparing vector databases for production RAG"
- "Look up this week's news about NVIDIA export controls"
- "Extract the main content from this article URL"

## Notes

- Needs `AISA_API_KEY` from https://marketplace.aisa.one
- Powered by AIsa's unified API gateway (https://aisa.one)
- Use `--deep` for complex research questions
- Use `--topic news` for current events
