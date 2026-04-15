# AIsa Agent Skills Index

这份索引面向正式发布仓库：

- Repository: <https://github.com/AIsa-team/agent-skills>
- Branch: `agentskills`
- Branch URL: <https://github.com/AIsa-team/agent-skills/tree/agentskills>

当前整理完成的 skills 如下。

## Twitter / X

### `aisa-twitter-command-center`

- GitHub: <https://github.com/AIsa-team/agent-skills/tree/agentskills/aisa-twitter-command-center>
- Summary: Search X/Twitter profiles, tweets, trends, lists, communities, and Spaces through the AIsa relay, then support approved posting workflows with OAuth.
- Includes:
  - `scripts/twitter_client.py`
  - `scripts/twitter_oauth_client.py`
  - `references/post_twitter.md`

### `aisa-twitter-api`

- GitHub: <https://github.com/AIsa-team/agent-skills/tree/agentskills/aisa-twitter-api>
- Summary: Search X/Twitter profiles, tweets, trends, lists, communities, and Spaces through the AIsa relay, then support approved posting workflows with OAuth.
- Includes:
  - `scripts/twitter_client.py`
  - `scripts/twitter_oauth_client.py`
  - `references/post_twitter.md`

### `aisa-twitter-post-engage`

- GitHub: <https://github.com/AIsa-team/agent-skills/tree/agentskills/aisa-twitter-post-engage>
- Summary: Search X/Twitter profiles, tweets, trends, and approved engagement actions through the AIsa relay, including posting, likes, follows, and related workflows.
- Includes:
  - `scripts/twitter_client.py`
  - `scripts/twitter_oauth_client.py`
  - `scripts/twitter_engagement_client.py`
  - `references/post_twitter.md`
  - `references/engage_twitter.md`

### `aisa-twitter-engagement-suite`

- GitHub: <https://github.com/AIsa-team/agent-skills/tree/agentskills/aisa-twitter-engagement-suite>
- Summary: Search X/Twitter profiles, tweets, trends, and approved engagement actions through the AIsa relay, with a bundled engagement workflow suite.
- Includes:
  - `scripts/twitter_client.py`
  - `scripts/twitter_oauth_client.py`
  - `scripts/twitter_engagement_client.py`
  - `references/post_twitter.md`
  - `references/engage_twitter.md`

### `x-intelligence-automation`

- GitHub: <https://github.com/AIsa-team/agent-skills/tree/agentskills/x-intelligence-automation>
- Summary: Search X/Twitter profiles, tweets, trends, and approved engagement actions through the AIsa relay, packaged under the X Intelligence Automation brand.
- Includes:
  - `scripts/twitter_client.py`
  - `scripts/twitter_oauth_client.py`
  - `scripts/twitter_engagement_client.py`
  - `references/post_twitter.md`
  - `references/engage_twitter.md`

## YouTube

### `aisa-youtube-search`

- GitHub: <https://github.com/AIsa-team/agent-skills/tree/agentskills/aisa-youtube-search>
- Summary: Search YouTube videos, channels, and playlists through the AIsa YouTube relay with one API key.
- Includes:
  - `SKILL.md`
  - `README.md`
  - `LICENSE.txt`

### `aisa-youtube-serp-scout`

- GitHub: <https://github.com/AIsa-team/agent-skills/tree/agentskills/aisa-youtube-serp-scout>
- Summary: Search YouTube videos, channels, and trends through the AIsa YouTube SERP client for content research, competitor tracking, and trend discovery.
- Includes:
  - `scripts/youtube_client.py`
  - `SKILL.md`
  - `README.md`

### `youtube`

- GitHub: <https://github.com/AIsa-team/agent-skills/tree/agentskills/youtube>
- Summary: Search YouTube videos, channels, and trends for content research and competitor tracking.
- Includes:
  - `scripts/youtube_client.py`
  - `SKILL.md`
  - `README.md`

## Search

### `search`

- GitHub: <https://github.com/AIsa-team/agent-skills/tree/agentskills/search>
- Summary: Run multi-source web, scholar, Tavily, and Perplexity-backed search workflows through AIsa.
- Includes:
  - `scripts/search_client.py`
  - `SKILL.md`
  - `README.md`

### `perplexity-search`

- GitHub: <https://github.com/AIsa-team/agent-skills/tree/agentskills/perplexity-search>
- Summary: Call Perplexity Sonar, Sonar Pro, Sonar Reasoning Pro, and Sonar Deep Research through AIsa.
- Includes:
  - `scripts/perplexity_search_client.py`
  - `SKILL.md`

## Finance

### `market`

- GitHub: <https://github.com/AIsa-team/agent-skills/tree/agentskills/market>
- Summary: Query real-time and historical financial data across equities and crypto for analysis, alerts, and reporting.
- Includes:
  - `scripts/market_client.py`
  - `SKILL.md`
  - `README.md`

## Prediction Markets

### `prediction-market`

- GitHub: <https://github.com/AIsa-team/agent-skills/tree/agentskills/prediction-market>
- Summary: Access Polymarket and Kalshi markets, prices, positions, and trades through AIsa.
- Includes:
  - `scripts/prediction_market_client.py`
  - `SKILL.md`
  - `README.md`

### `prediction-market-arbitrage`

- GitHub: <https://github.com/AIsa-team/agent-skills/tree/agentskills/prediction-market-arbitrage>
- Summary: Find and analyze arbitrage opportunities across prediction markets like Polymarket and Kalshi.
- Includes:
  - `scripts/arbitrage_finder.py`
  - `scripts/prediction_market_client.py`
  - `SKILL.md`
  - `README.md`

## Media

### `media-gen`

- GitHub: <https://github.com/AIsa-team/agent-skills/tree/agentskills/media-gen>
- Summary: Generate images and videos with AIsa through a single API key.
- Includes:
  - `scripts/media_gen_client.py`
  - `SKILL.md`
  - `README.md`

## Additional Twitter / X

### `twitter`

- GitHub: <https://github.com/AIsa-team/agent-skills/tree/agentskills/twitter>
- Summary: Search Twitter/X data and support approved posting and engagement workflows through the AIsa relay.
- Includes:
  - `scripts/twitter_client.py`
  - `scripts/twitter_oauth_client.py`
  - `scripts/twitter_engagement_client.py`
  - `references/post_twitter.md`
  - `references/engage_twitter.md`

## Recommended Publish Order

1. `aisa-twitter-command-center`
2. `aisa-twitter-post-engage`
3. `aisa-youtube-search`
4. `aisa-youtube-serp-scout`
5. `aisa-twitter-api`
6. `aisa-twitter-engagement-suite`
7. `x-intelligence-automation`
8. `search`
9. `perplexity-search`
10. `market`
11. `prediction-market`
12. `prediction-market-arbitrage`
13. `media-gen`
14. `twitter`
15. `youtube`

## Notes

- `aisa-twitter-command-center` 可以作为 Twitter 主推母版。
- `aisa-twitter-post-engage` 是能力更完整的读写一体版。
- `aisa-twitter-api` 与 `aisa-twitter-command-center` 能力接近，后续可以考虑收敛。
- `aisa-twitter-engagement-suite` 与 `x-intelligence-automation` 更适合作为品牌或渠道变体。
