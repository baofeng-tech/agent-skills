---
name: aisa-twitter-engagement-suite
description: 'Research Twitter/X profiles, tweets, trends, and approved engagement actions through the AIsa relay. Use when: the user needs Twitter/X research plus posting, likes, follows, or post-action follow-through without sharing passwords. Supports relay-based reads, OAuth-approved writes, and media-capable posting flows.'
license: MIT-0
compatibility: Designed for Agent Skills compatible clients such as OpenClaw, Claude Code, Hermes, and GitHub-backed skill catalogs. Requires system binaries python3, environment variables AISA_API_KEY and internet access to api.aisa.one.
metadata:
  author: AIsa
  version: 1.0.3
  homepage: https://aisa.one
  repository: https://github.com/baofeng-tech/agent-skills
  tags: twitter,x,search,research,media,aisa
  platforms: agentskills.io,agentskill.sh,github
  primary_env: AISA_API_KEY
allowed-tools: Read Bash Grep
---

# AIsa Twitter Engagement Suite

Research Twitter/X profiles, tweets, and trends, then run approved posting and engagement actions through the AIsa relay.

## When to use

- When the user needs Twitter/X research plus action-oriented follow-through such as posting, liking, unliking, following, or unfollowing.
- When the workflow can use a Python client with `AISA_API_KEY` and network access to `api.aisa.one`.
- When the task needs relay-based Twitter/X writes without asking the user to share passwords.
- When the user can complete explicit OAuth approval before write actions or media posting.

## When NOT to use

- Do not use this for cookie extraction, password login, or a fully local Twitter client.
- Do not use this when the workflow must avoid relay-based network calls, remote writes, or media upload through `api.aisa.one`.
- Do not use this for undocumented secrets, browser-derived auth values, or hidden credential flows.
- Do not use this when the user only needs the broader flagship Twitter lane; use `aisa-twitter-api` for that surface.

## Quick Reference

| Need | Path / Requirement |
| --- | --- |
| API key | `AISA_API_KEY` |
| Required binary | `python3` |
| Relay target | `api.aisa.one` |
| Read client | `scripts/twitter_client.py` |
| Post client | `scripts/twitter_oauth_client.py` |
| Engage client | `scripts/twitter_engagement_client.py` |
| References | `references/post_twitter.md`, `references/engage_twitter.md` |

## Setup

```bash
export AISA_API_KEY="your-key"
```

Requirements:

- `python3`
- Internet access to `api.aisa.one`
- Explicit OAuth approval before posting or engagement writes
- Relay-based upload support for approved media posting flows

## Common Commands

```bash
python3 scripts/twitter_client.py search --query "AI agents" --type Latest
python3 scripts/twitter_oauth_client.py authorize
python3 scripts/twitter_engagement_client.py like-latest --user "@elonmusk"
```

## Capabilities

- Research Twitter/X accounts, tweets, trends, lists, communities, and Spaces.
- Publish text, image, and video posts after explicit OAuth approval.
- Like, unlike, follow, and unfollow after authorization exists.
- Keep read and write workflows in one package while making relay, approval, and upload requirements explicit.

## Trust and Side Effects

- All networked operations go through the AIsa relay at `api.aisa.one`.
- Write actions require explicit OAuth approval before they can succeed.
- Posting with media uses relay-based upload paths supported by the runtime.
- Reads, writes, and uploads are remote API operations, not local-only actions.
- Do not claim a post, like, follow, or unfollow succeeded until the API confirms it.
