---
name: aisa-twitter-api
description: 'Twitter/X research, monitoring, watchlists, and OAuth-approved posting through AIsa. Use when: the user needs one flagship Twitter skill for trend tracking, competitor monitoring, timeline analysis, or approved posting without sharing passwords. Supports search, watchlists, relay-based reads, and OAuth-gated text or media posting.'
license: Apache-2.0
compatibility: Designed for Agent Skills compatible clients such as OpenClaw, Claude Code, Hermes, and GitHub-backed skill catalogs. Requires system binaries python3, environment variables AISA_API_KEY and internet access to api.aisa.one.
metadata:
  author: AIsa
  version: 1.0.5
  homepage: https://aisa.one
  repository: https://github.com/baofeng-tech/agent-skills
  tags: twitter,x,search,research,media,aisa
  platforms: agentskills.io,agentskill.sh,github
  primary_env: AISA_API_KEY
allowed-tools: Read Bash Grep
---

# AIsa Twitter API Command Center

Use one AIsa-backed Twitter/X surface for research, monitoring, watchlists, and OAuth-approved posting.

## When to use

- The user wants one flagship Twitter/X skill for research, monitoring, trend discovery, or content discovery.
- The user wants to inspect profiles, timelines, mentions, trends, replies, quotes, lists, communities, or Spaces.
- The user wants to draft or publish posts after explicit OAuth approval without sharing passwords.
- The user needs a relay-based Twitter/X workflow that uses `AISA_API_KEY` instead of local password or cookie access.

## When NOT to use

- The user needs password-based login, cookie extraction, or browser credential scraping.
- The workflow must avoid relay-based calls to `api.aisa.one`.
- The request centers on likes, follows, replies, or growth actions better handled by `aisa-twitter-engagement-suite`.

## Quick Reference

- Required environment variable: `AISA_API_KEY`
- Required binary: `python3`
- Read client: `scripts/twitter_client.py`
- OAuth and posting client: `scripts/twitter_oauth_client.py`
- Posting guide: `references/post_twitter.md`
- Relay target: `https://api.aisa.one`
- External writes: posting happens only after explicit OAuth approval
- Upload behavior: image and video posting sends user-selected media through the relay

## Setup

```bash
export AISA_API_KEY="your-key"
```

Requirements:

- `python3`
- Internet access to `https://api.aisa.one`
- OAuth approval before posting
- User-provided media files when posting images or videos

## Capabilities

- Read user data, timelines, mentions, followers, followings, and related profile information.
- Search tweets and users, inspect replies, quotes, retweeters, thread context, trends, lists, communities, and Spaces.
- Support watchlist-style research and monitoring workflows.
- Publish text, image, and video posts after explicit OAuth approval.

## High-Intent Workflows

- Research a creator, competitor, or narrative before writing.
- Monitor a keyword, launch, or watchlist and pull supporting tweets fast.
- Review timelines, mentions, replies, and trend movement from one command surface.
- Draft and publish a post only after the user explicitly approves OAuth.

## Common Commands

```bash
python3 scripts/twitter_client.py search --query "AI agents" --type Latest
python3 scripts/twitter_oauth_client.py authorize
python3 scripts/twitter_oauth_client.py post --text "Hello from AIsa"
```

## Guardrails

- Do not ask for Twitter passwords or browser cookies.
- Do not invent captions, tweet URLs, or attachment files.
- Do not claim external posting succeeded until the API confirms success.
- Do not imply OAuth is optional for posting.

## Example Requests

- Research what builders on X are saying about AI agents this week.
- Track reactions to our product launch and pull representative tweets.
- Build a small watchlist of competitor accounts and summarize what changed today.
- Authorize and publish a short Twitter post with an attached image.

## Security Notes

- This is a relay-based workflow that sends Twitter/X API requests to `https://api.aisa.one`.
- Posting requires explicit OAuth approval through the relay before external writes occur.
- Approved image and video posting sends user-selected media through the relay for upload.
- Required secret: `AISA_API_KEY`.
- This workflow does not require passwords or browser cookie extraction.
