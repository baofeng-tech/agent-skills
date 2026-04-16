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

### `aisa-tavily`

- GitHub: <https://github.com/AIsa-team/agent-skills/tree/agentskills/aisa-tavily>
- Summary: Run Tavily-backed AI web search and URL extraction through AIsa.
- Includes:
  - `scripts/search.mjs`
  - `scripts/extract.mjs`
  - `SKILL.md`

## LLM / Providers

### `llm-router`

- GitHub: <https://github.com/AIsa-team/agent-skills/tree/agentskills/llm-router>
- Summary: Route prompts across GPT, Claude, Gemini, Qwen, DeepSeek, and other models through AIsa's OpenAI-compatible gateway.
- Includes:
  - `scripts/llm_router_client.py`
  - `SKILL.md`
  - `README.md`

### `aisa-provider`

- GitHub: <https://github.com/AIsa-team/agent-skills/tree/agentskills/aisa-provider>
- Summary: Configure AIsa as an OpenClaw provider for Chinese model access, pricing, and setup workflows.
- Includes:
  - `references/config-examples.md`
  - `references/guide-zh-CN.md`
  - `references/pricing.md`
  - `SKILL.md`

### `cn-llm`

- GitHub: <https://github.com/AIsa-team/agent-skills/tree/agentskills/cn-llm>
- Summary: Access Qwen, DeepSeek, GLM, Baichuan, and related Chinese LLMs through AIsa.
- Includes:
  - `scripts/cn_llm_client.py`
  - `SKILL.md`
  - `README.md`

## Finance

### `market`

- GitHub: <https://github.com/AIsa-team/agent-skills/tree/agentskills/market>
- Summary: Query real-time and historical financial data across equities and crypto for analysis, alerts, and reporting.
- Includes:
  - `scripts/market_client.py`
  - `SKILL.md`
  - `README.md`

### `us-stock-analyst`

- GitHub: <https://github.com/AIsa-team/agent-skills/tree/agentskills/us-stock-analyst>
- Summary: Run US stock analysis workflows combining market data, news, sentiment, and multi-model AI through AIsa.
- Includes:
  - `scripts/stock_analyst.py`
  - `requirements.txt`
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

### `prediction-market-arbitrage-api`

- GitHub: <https://github.com/AIsa-team/agent-skills/tree/agentskills/prediction-market-arbitrage-api>
- Summary: Scan Polymarket and Kalshi for arbitrage opportunities through the AIsa API.
- Includes:
  - `scripts/arbitrage_finder.py`
  - `scripts/prediction_market_client.py`
  - `SKILL.md`

### `prediction-market-data-zh`

- GitHub: <https://github.com/AIsa-team/agent-skills/tree/agentskills/prediction-market-data-zh>
- Summary: 中文预测市场数据查询，通过 AIsa 访问 Polymarket 和 Kalshi。
- Includes:
  - `scripts/prediction_market_client.py`
  - `SKILL.md`

### `prediction-market-arbitrage-zh`

- GitHub: <https://github.com/AIsa-team/agent-skills/tree/agentskills/prediction-market-arbitrage-zh>
- Summary: 中文预测市场套利分析，通过 AIsa 扫描 Polymarket 与 Kalshi 价差。
- Includes:
  - `scripts/arbitrage_finder.py`
  - `scripts/prediction_market_client.py`
  - `SKILL.md`

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
16. `aisa-tavily`
17. `llm-router`
18. `aisa-provider`
19. `cn-llm`
20. `us-stock-analyst`
21. `prediction-market-arbitrage-api`
22. `prediction-market-data-zh`
23. `prediction-market-arbitrage-zh`

## Imported Name-Preserved Variants

### `last30days`

- GitHub: <https://github.com/AIsa-team/agent-skills/tree/agentskills/last30days>
- Summary: Research the last 30 days across Reddit, X/Twitter, YouTube, TikTok, Instagram, Hacker News, Polymarket, GitHub, and web search. Use when: you need recent social research, company updates, person profiles, competitor comparisons, launch reactions, or trend scans. Supports AISA-powered planning, clustering, reranking, and JSON output.
- Includes:
  - `scripts/briefing.py`
  - `scripts/compare.sh`
  - `scripts/dev-python.sh`
  - `scripts/evaluate_search_quality.py`

### `last30days-zh`

- GitHub: <https://github.com/AIsa-team/agent-skills/tree/agentskills/last30days-zh>
- Summary: 聚合最近 30 天的 Reddit、X/Twitter、YouTube、TikTok、Instagram、Hacker News、Polymarket、GitHub 和 web search 结果。触发条件：当用户需要 recent social research、人物近况、公司动态、竞品对比、发布反应、趋势扫描时使用。支持 AISA 规划、聚类、重排和 JSON 输出。
- Includes:
  - `scripts/briefing.py`
  - `scripts/compare.sh`
  - `scripts/dev-python.sh`
  - `scripts/evaluate_search_quality.py`

### `marketpulse`

- GitHub: <https://github.com/AIsa-team/agent-skills/tree/agentskills/marketpulse>
- Summary: Query real-time and historical financial data across equities and crypto—prices, market moves, metrics, and trends for analysis, alerts, and reporting.
- Includes:
  - `scripts/market_client.py`
  - `README.md`

### `openclaw-aisa-youtube-aisa`

- GitHub: <https://github.com/AIsa-team/agent-skills/tree/agentskills/openclaw-aisa-youtube-aisa>
- Summary: Search YouTube videos, channels, and trends through the AISA YouTube SERP client. Use when: the user asks for content research, competitor tracking, or trend discovery without managing Google credentials. Supports curl queries and the bundled Python client with locale and filter controls.
- Includes:
  - `scripts/youtube_client.py`

### `openclaw-media-gen`

- GitHub: <https://github.com/AIsa-team/agent-skills/tree/agentskills/openclaw-media-gen>
- Summary: Generate images & videos with AIsa. Gemini 3 Pro Image (image) + Qwen Wan 2.6 (video) via one API key.
- Includes:
  - `scripts/media_gen_client.py`
  - `README.md`

### `openclaw-search`

- GitHub: <https://github.com/AIsa-team/agent-skills/tree/agentskills/openclaw-search>
- Summary: Intelligent search for agents. Multi-source retrieval with confidence scoring - web, academic, and Tavily in one unified API.
- Includes:
  - `scripts/search_client.py`
  - `README.md`

### `openclaw-twitter`

- GitHub: <https://github.com/AIsa-team/agent-skills/tree/agentskills/openclaw-twitter>
- Summary: Search X/Twitter profiles, tweets, trends, lists, communities, and Spaces through the AISA relay, then publish approved posts with OAuth. Use when: the user asks for Twitter/X research, monitoring, or posting without sharing passwords. Supports read APIs, authorization links, and media-aware posting.
- Includes:
  - `scripts/twitter_client.py`
  - `scripts/twitter_oauth_client.py`
  - `references/post_twitter.md`

### `openclaw-twitter-post-engage`

- GitHub: <https://github.com/AIsa-team/agent-skills/tree/agentskills/openclaw-twitter-post-engage>
- Summary: Search X/Twitter profiles, tweets, trends, and approved engagement actions through the AISA relay. Use when: the user asks for Twitter/X research, posting, likes, follows, or related workflows without sharing passwords. Supports read APIs, OAuth-gated posting, and follow or like operations.
- Includes:
  - `scripts/twitter_client.py`
  - `scripts/twitter_engagement_client.py`
  - `scripts/twitter_oauth_client.py`
  - `references/engage_twitter.md`

### `openclaw-youtube`

- GitHub: <https://github.com/AIsa-team/agent-skills/tree/agentskills/openclaw-youtube>
- Summary: YouTube SERP Scout for agents. Search top-ranking videos, channels, and trends for content research and competitor tracking.
- Includes:
  - `scripts/youtube_client.py`
  - `README.md`

### `prediction-market-data`

- GitHub: <https://github.com/AIsa-team/agent-skills/tree/agentskills/prediction-market-data>
- Summary: Cross-platform prediction market data via AIsa API. Query Polymarket and Kalshi markets, prices, orderbooks, candlesticks, positions, and trades. Use when user asks about: prediction market odds, election betting, event probabilities, market sentiment, Polymarket prices, Kalshi prices, sports betting odds, wallet PnL, or cross-platform market comparison.
- Includes:
  - `scripts/prediction_market_client.py`

### `twitter-command-center-search-post`

- GitHub: <https://github.com/AIsa-team/agent-skills/tree/agentskills/twitter-command-center-search-post>
- Summary: Searches and reads X (Twitter): profiles, timelines, mentions, followers, tweet search, trends, lists, communities, and Spaces. Publishes posts after the user completes OAuth in the browser. Use when the user asks about Twitter/X data, social listening, or posting without sharing account passwords.
- Includes:
  - `scripts/twitter_client.py`
  - `scripts/twitter_oauth_client.py`
  - `references/post_twitter.md`
  - `README.md`

### `twitter-command-center-search-post-interact`

- GitHub: <https://github.com/AIsa-team/agent-skills/tree/agentskills/twitter-command-center-search-post-interact>
- Summary: Searches and reads X (Twitter): profiles, timelines, mentions, followers, tweet search, trends, lists, communities, and Spaces. Publishes posts, likes/unlikes tweets, and follows/unfollows users after the user completes OAuth in the browser. Use when the user asks about Twitter/X data, social listening, posting, or interacting with tweets/users without sharing account passwords.
- Includes:
  - `scripts/twitter_client.py`
  - `scripts/twitter_engagement_client.py`
  - `scripts/twitter_oauth_client.py`
  - `references/engage_twitter.md`

### `youtube-search`

- GitHub: <https://github.com/AIsa-team/agent-skills/tree/agentskills/youtube-search>
- Summary: |
- Includes:
  - `LICENSE.txt`

## Notes

- `aisa-twitter-command-center` 可以作为 Twitter 主推母版。
- `aisa-twitter-post-engage` 是能力更完整的读写一体版。
- `aisa-twitter-api` 与 `aisa-twitter-command-center` 能力接近，后续可以考虑收敛。
- `aisa-twitter-engagement-suite` 与 `x-intelligence-automation` 更适合作为品牌或渠道变体。
