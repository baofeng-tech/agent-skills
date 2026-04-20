# AIsa Agent Skills Index

This index is prepared for the public Agent Skills repository used by AgentSkills.so-style crawlers.

- Repository: <https://github.com/baofeng-tech/agent-skills>
- Branch: `main`
- Branch URL: <https://github.com/baofeng-tech/agent-skills/tree/main>

## Skills

### `aisa-multi-search-engine`

- GitHub: <https://github.com/baofeng-tech/agent-skills/tree/main/aisa-multi-search-engine>
- Summary: Multi-source search engine powered by AIsa API. Combines Tavily web search, Scholar academic search, Smart hybrid search, and Perplexity deep research — all through a single AIsa API key. Includes confidence scoring and AI synthesis. Use when: the user needs web search, research, source discovery, or content extraction.
- Includes:
  - `scripts/search_client.py`
  - `SKILL.md`
  - `README.md`

### `aisa-provider`

- GitHub: <https://github.com/baofeng-tech/agent-skills/tree/main/aisa-provider>
- Summary: Configure AIsa as a first-class model provider for OpenClaw, enabling production access to major Chinese AI models (Qwen, DeepSeek, Kimi K2.5, Doubao) through official partnerships with Alibaba Cloud, BytePlus, and Moonshot. Use this skill when the user wants to set up Chinese AI models, configure AIsa API access, compare pricing between AIsa and other providers (OpenRouter, Bailian), switch between Qwen/DeepSeek/Kimi models, or troubleshoot AIsa provider configuration in OpenClaw. Also use when the user mentions AISA_API_KEY, asks about Chinese LLM pricing, Kimi K2.5 setup, or needs help with Qwen Key Account setup.
- Includes:
  - `references/config-examples.md`
  - `references/guide-zh-CN.md`
  - `references/pricing.md`
  - `SKILL.md`
  - `README.md`

### `aisa-tavily`

- GitHub: <https://github.com/baofeng-tech/agent-skills/tree/main/aisa-tavily>
- Summary: AI-optimized web search via AIsa's Tavily API proxy. Returns concise, relevant results for AI agents through AIsa's unified API gateway. Use when: the user needs web search, research, source discovery, or content extraction.
- Includes:
  - `scripts/extract.mjs`
  - `scripts/search.mjs`
  - `SKILL.md`
  - `README.md`

### `aisa-twitter-api`

- GitHub: <https://github.com/baofeng-tech/agent-skills/tree/main/aisa-twitter-api>
- Summary: Search X/Twitter profiles, tweets, trends, lists, communities, and Spaces through the AIsa relay, then support approved posting workflows with OAuth. Use when the user asks for Twitter research, monitoring, or posting without sharing passwords.
- Includes:
  - `scripts/twitter_client.py`
  - `scripts/twitter_oauth_client.py`
  - `references/post_twitter.md`
  - `SKILL.md`
  - `README.md`

### `aisa-twitter-command-center`

- GitHub: <https://github.com/baofeng-tech/agent-skills/tree/main/aisa-twitter-command-center>
- Summary: Search X/Twitter profiles, tweets, trends, lists, communities, and Spaces through the AIsa relay, then support approved posting workflows with OAuth. Use when the user asks for Twitter research, monitoring, or posting without sharing passwords.
- Includes:
  - `scripts/twitter_client.py`
  - `scripts/twitter_oauth_client.py`
  - `references/post_twitter.md`
  - `SKILL.md`
  - `README.md`

### `aisa-twitter-engagement-suite`

- GitHub: <https://github.com/baofeng-tech/agent-skills/tree/main/aisa-twitter-engagement-suite>
- Summary: Search X/Twitter profiles, tweets, trends, and approved engagement actions through the AIsa relay. Use when the user asks for Twitter/X research, posting, likes, follows, or related workflows without sharing passwords.
- Includes:
  - `scripts/twitter_client.py`
  - `scripts/twitter_engagement_client.py`
  - `scripts/twitter_oauth_client.py`
  - `references/engage_twitter.md`
  - `references/post_twitter.md`

### `aisa-twitter-post-engage`

- GitHub: <https://github.com/baofeng-tech/agent-skills/tree/main/aisa-twitter-post-engage>
- Summary: Search X/Twitter profiles, tweets, trends, and approved engagement actions through the AIsa relay. Use when the user asks for Twitter/X research, posting, likes, follows, or related workflows without sharing passwords.
- Includes:
  - `scripts/twitter_client.py`
  - `scripts/twitter_engagement_client.py`
  - `scripts/twitter_oauth_client.py`
  - `references/engage_twitter.md`
  - `references/post_twitter.md`

### `aisa-youtube-search`

- GitHub: <https://github.com/baofeng-tech/agent-skills/tree/main/aisa-youtube-search>
- Summary: Search YouTube videos, channels, and playlists through the AIsa YouTube relay with one API key. Use when the user asks for YouTube discovery, query expansion, or pagination without managing Google credentials.
- Includes:
  - `SKILL.md`
  - `README.md`

### `aisa-youtube-serp-scout`

- GitHub: <https://github.com/baofeng-tech/agent-skills/tree/main/aisa-youtube-serp-scout>
- Summary: Search YouTube videos, channels, and trends through the AIsa YouTube SERP client. Use when the user asks for content research, competitor tracking, or trend discovery without managing Google credentials. Use when: the user needs YouTube search, trend discovery, channel research, or SERP analysis.
- Includes:
  - `scripts/youtube_client.py`
  - `SKILL.md`
  - `README.md`

### `cn-llm`

- GitHub: <https://github.com/baofeng-tech/agent-skills/tree/main/cn-llm>
- Summary: China LLM Gateway - Unified interface for Chinese LLMs including Qwen, DeepSeek, GLM, Baichuan. OpenAI compatible, one API Key for all models. Use when: the user needs model routing, provider setup, or Chinese LLM access guidance.
- Includes:
  - `scripts/cn_llm_client.py`
  - `SKILL.md`
  - `README.md`

### `last30days`

- GitHub: <https://github.com/baofeng-tech/agent-skills/tree/main/last30days>
- Summary: Research the last 30 days across Reddit, X/Twitter, YouTube, TikTok, Instagram, Hacker News, Polymarket, and web search. Use when: the user needs recent multi-source research across the last 30 days.
- Includes:
  - `scripts/last30days.py`
  - `scripts/lib/__init__.py`
  - `scripts/lib/aisa.py`
  - `scripts/lib/cluster.py`
  - `scripts/lib/dates.py`

### `last30days-zh`

- GitHub: <https://github.com/baofeng-tech/agent-skills/tree/main/last30days-zh>
- Summary: 聚合最近 30 天的 Reddit、X/Twitter、YouTube、TikTok、Instagram、Hacker News、Polymarket 和 web search 结果. Use when: the user needs recent multi-source research across the last 30 days.
- Includes:
  - `scripts/last30days.py`
  - `scripts/lib/__init__.py`
  - `scripts/lib/aisa.py`
  - `scripts/lib/cluster.py`
  - `scripts/lib/dates.py`

### `llm-router`

- GitHub: <https://github.com/baofeng-tech/agent-skills/tree/main/llm-router>
- Summary: Unified LLM Gateway - One API for 70+ AI models. Route to GPT, Claude, Gemini, Qwen, Deepseek, Grok and more with a single API key. Use when: the user needs model routing, provider setup, or Chinese LLM access guidance.
- Includes:
  - `scripts/llm_router_client.py`
  - `SKILL.md`
  - `README.md`

### `market`

- GitHub: <https://github.com/baofeng-tech/agent-skills/tree/main/market>
- Summary: Query real-time and historical financial data across equities and crypto—prices, market moves, metrics, and trends for analysis, alerts, and reporting. Use when: the user needs market data, stock analysis, watchlists, or portfolio workflows.
- Includes:
  - `scripts/market_client.py`
  - `SKILL.md`
  - `README.md`

### `marketpulse`

- GitHub: <https://github.com/baofeng-tech/agent-skills/tree/main/marketpulse>
- Summary: Query real-time and historical financial data across equities and crypto—prices, market moves, metrics, and trends for analysis, alerts, and reporting. Use when: the user needs market data, stock analysis, watchlists, or portfolio workflows.
- Includes:
  - `scripts/market_client.py`
  - `SKILL.md`
  - `README.md`

### `media-gen`

- GitHub: <https://github.com/baofeng-tech/agent-skills/tree/main/media-gen>
- Summary: Generate images & videos with AIsa. Gemini 3 Pro Image (image) + Qwen Wan 2.6 (video) via one API key. Use when: the user needs AI image or video generation workflows.
- Includes:
  - `scripts/media_gen_client.py`
  - `SKILL.md`
  - `README.md`

### `multi-search`

- GitHub: <https://github.com/baofeng-tech/agent-skills/tree/main/multi-search>
- Summary: Parallel multi-source search combining Web, Scholar, Smart, and Tavily results with confidence scoring and AI synthesis. Best for comprehensive research requiring cross-source validation. Use when: the user needs web search, research, source discovery, or content extraction.
- Includes:
  - `scripts/search_client.py`
  - `SKILL.md`
  - `README.md`

### `openclaw-aisa-youtube-aisa`

- GitHub: <https://github.com/baofeng-tech/agent-skills/tree/main/openclaw-aisa-youtube-aisa>
- Summary: Search YouTube videos, channels, and trends through the AISA YouTube SERP client. Use when: the user needs YouTube search, trend discovery, channel research, or SERP analysis.
- Includes:
  - `scripts/youtube_client.py`
  - `SKILL.md`
  - `README.md`

### `openclaw-media-gen`

- GitHub: <https://github.com/baofeng-tech/agent-skills/tree/main/openclaw-media-gen>
- Summary: Generate images & videos with AIsa. Gemini 3 Pro Image (image) + Qwen Wan 2.6 (video) via one API key. Use when: the user needs AI image or video generation workflows.
- Includes:
  - `scripts/media_gen_client.py`
  - `SKILL.md`
  - `README.md`

### `openclaw-search`

- GitHub: <https://github.com/baofeng-tech/agent-skills/tree/main/openclaw-search>
- Summary: Intelligent search for agents. Multi-source retrieval with confidence scoring - web, academic, and Tavily in one unified API. Use when: the user needs web search, research, source discovery, or content extraction.
- Includes:
  - `scripts/search_client.py`
  - `SKILL.md`
  - `README.md`

### `openclaw-twitter`

- GitHub: <https://github.com/baofeng-tech/agent-skills/tree/main/openclaw-twitter>
- Summary: Search X/Twitter profiles, tweets, trends, lists, communities, and Spaces through the AISA relay, then publish approved posts with OAuth. Use when: the user asks for Twitter/X research, monitoring, or posting without sharing passwords. Supports read APIs, authorization links, and media-aware posting.
- Includes:
  - `scripts/twitter_client.py`
  - `scripts/twitter_oauth_client.py`
  - `references/post_twitter.md`
  - `SKILL.md`
  - `README.md`

### `openclaw-twitter-post-engage`

- GitHub: <https://github.com/baofeng-tech/agent-skills/tree/main/openclaw-twitter-post-engage>
- Summary: Search X/Twitter profiles, tweets, trends, and approved engagement actions through the AISA relay. Use when: the user asks for Twitter/X research, posting, likes, follows, or related workflows without sharing passwords. Supports read APIs, OAuth-gated posting, and follow or like operations.
- Includes:
  - `scripts/twitter_client.py`
  - `scripts/twitter_engagement_client.py`
  - `scripts/twitter_oauth_client.py`
  - `references/engage_twitter.md`
  - `references/post_twitter.md`

### `openclaw-youtube`

- GitHub: <https://github.com/baofeng-tech/agent-skills/tree/main/openclaw-youtube>
- Summary: YouTube SERP Scout for agents. Search top-ranking videos, channels, and trends for content research and competitor tracking. Use when: the user needs YouTube search, trend discovery, channel research, or SERP analysis.
- Includes:
  - `scripts/youtube_client.py`
  - `SKILL.md`
  - `README.md`

### `perplexity-research`

- GitHub: <https://github.com/baofeng-tech/agent-skills/tree/main/perplexity-research>
- Summary: Deep research using Perplexity Sonar models via AIsa API. Provides synthesized answers with citations. Supports 4 models from fast to exhaustive deep research. Use when: the user needs web search, research, source discovery, or content extraction.
- Includes:
  - `scripts/search_client.py`
  - `SKILL.md`
  - `README.md`

### `perplexity-search`

- GitHub: <https://github.com/baofeng-tech/agent-skills/tree/main/perplexity-search>
- Summary: Perplexity Sonar search and answer generation through AIsa. Use when the task is specifically to call Perplexity Sonar, Sonar Pro, Sonar Reasoning Pro, or Sonar Deep Research for citation-backed web answers, analytical reasoning, or long-form research reports.
- Includes:
  - `scripts/perplexity_search_client.py`
  - `SKILL.md`
  - `README.md`

### `prediction-market`

- GitHub: <https://github.com/baofeng-tech/agent-skills/tree/main/prediction-market>
- Summary: Prediction markets data - Polymarket, Kalshi markets, prices, positions, and trades. Use when: the user needs market data, stock analysis, watchlists, or portfolio workflows.
- Includes:
  - `scripts/prediction_market_client.py`
  - `SKILL.md`
  - `README.md`

### `prediction-market-arbitrage`

- GitHub: <https://github.com/baofeng-tech/agent-skills/tree/main/prediction-market-arbitrage>
- Summary: Find and analyze arbitrage opportunities across prediction markets like Polymarket and Kalshi. Use when: the user needs market data, stock analysis, watchlists, or portfolio workflows.
- Includes:
  - `scripts/arbitrage_finder.py`
  - `scripts/prediction_market_client.py`
  - `SKILL.md`
  - `README.md`

### `prediction-market-arbitrage-api`

- GitHub: <https://github.com/baofeng-tech/agent-skills/tree/main/prediction-market-arbitrage-api>
- Summary: Find arbitrage opportunities across Polymarket and Kalshi prediction markets via AIsa API. Scan sports markets for cross-platform price discrepancies, compare real-time odds, verify orderbook liquidity. Use when user asks about: prediction market arbitrage, cross-platform price differences, sports betting arbitrage, odds comparison, risk-free profit, market inefficiencies.
- Includes:
  - `scripts/arbitrage_finder.py`
  - `scripts/prediction_market_client.py`
  - `SKILL.md`
  - `README.md`

### `prediction-market-arbitrage-zh`

- GitHub: <https://github.com/baofeng-tech/agent-skills/tree/main/prediction-market-arbitrage-zh>
- Summary: 通过 AIsa API 发现 Polymarket 和 Kalshi 预测市场的套利机会。扫描体育市场跨平台价差、比较实时赔率、验证订单簿流动性。适用场景：预测市场套利、跨平台价差、体育博彩套利、赔率对比、无风险利润、市场低效。 Use when: the user needs market data, stock analysis, watchlists, or portfolio workflows.
- Includes:
  - `scripts/arbitrage_finder.py`
  - `scripts/prediction_market_client.py`
  - `SKILL.md`
  - `README.md`

### `prediction-market-data`

- GitHub: <https://github.com/baofeng-tech/agent-skills/tree/main/prediction-market-data>
- Summary: Cross-platform prediction market data via AIsa API. Query Polymarket and Kalshi markets, prices, orderbooks, candlesticks, positions, and trades. Use when user asks about: prediction market odds, election betting, event probabilities, market sentiment, Polymarket prices, Kalshi prices, sports betting odds, wallet PnL, or cross-platform market comparison.
- Includes:
  - `scripts/prediction_market_client.py`
  - `SKILL.md`
  - `README.md`

### `prediction-market-data-zh`

- GitHub: <https://github.com/baofeng-tech/agent-skills/tree/main/prediction-market-data-zh>
- Summary: 通过 AIsa API 查询跨平台预测市场数据。支持 Polymarket 和 Kalshi 的市场行情、价格、订单簿、K线、持仓和交易记录。适用场景：查询预测市场赔率、选举博彩、事件概率、市场情绪、Polymarket 价格、Kalshi 价格、体育博彩赔率、钱包盈亏、跨平台市场对比。 Use when: the user needs market data, stock analysis, watchlists, or portfolio workflows.
- Includes:
  - `scripts/prediction_market_client.py`
  - `SKILL.md`
  - `README.md`

### `scholar-search`

- GitHub: <https://github.com/baofeng-tech/agent-skills/tree/main/scholar-search>
- Summary: Search academic papers and scholarly articles via AIsa Scholar endpoint. Supports year range filtering for targeted research. Use when: the user needs web search, research, source discovery, or content extraction.
- Includes:
  - `scripts/search_client.py`
  - `SKILL.md`
  - `README.md`

### `search`

- GitHub: <https://github.com/baofeng-tech/agent-skills/tree/main/search>
- Summary: Intelligent search for agents. Multi-source retrieval across web, scholar, Tavily, and Perplexity Sonar models. Use when: the user needs web search, research, source discovery, or content extraction.
- Includes:
  - `scripts/search_client.py`
  - `SKILL.md`
  - `README.md`

### `smart-search`

- GitHub: <https://github.com/baofeng-tech/agent-skills/tree/main/smart-search>
- Summary: Intelligent hybrid search combining web and academic sources via AIsa Smart Search endpoint. Best when you need both web and scholarly results. Use when: the user needs web search, research, source discovery, or content extraction.
- Includes:
  - `scripts/search_client.py`
  - `SKILL.md`
  - `README.md`

### `stock-analysis`

- GitHub: <https://github.com/baofeng-tech/agent-skills/tree/main/stock-analysis>
- Summary: Analyze stocks and cryptocurrencies with 8-dimension scoring via AIsa API. Provides BUY/HOLD/SELL signals with confidence levels, entry/target/stop prices, and risk flags. Supports single or multi-ticker analysis with optional fast mode and JSON output. Use when the user asks to analyze a stock, check a ticker, or compare investments.
- Includes:
  - `scripts/analyze_stock.py`
  - `SKILL.md`
  - `README.md`

### `stock-dividend`

- GitHub: <https://github.com/baofeng-tech/agent-skills/tree/main/stock-dividend>
- Summary: Analyze dividend metrics for stocks via AIsa API. Provides yield, payout ratio, growth CAGR, safety score (0-100), income rating, and Dividend Aristocrat/King status. Use when the user asks about dividends, income investing, or dividend safety.
- Includes:
  - `scripts/dividends.py`
  - `SKILL.md`
  - `README.md`

### `stock-hot`

- GitHub: <https://github.com/baofeng-tech/agent-skills/tree/main/stock-hot>
- Summary: Hot Scanner — find the most trending and high-momentum stocks and crypto right now via AIsa API. Top gainers, losers, most active by volume, crypto highlights, news catalysts, and top 5 watchlist picks. Use when the user asks about trending stocks, what's hot, market movers, or momentum plays.
- Includes:
  - `scripts/hot_scanner.py`
  - `SKILL.md`
  - `README.md`

### `stock-portfolio`

- GitHub: <https://github.com/baofeng-tech/agent-skills/tree/main/stock-portfolio>
- Summary: Manage investment portfolios with live P&L tracking via AIsa API. Create, add, update, remove positions, rename, and show portfolio summary with real-time profit/loss. Use when the user wants to track investments, manage a portfolio, check P&L, or add/remove holdings.
- Includes:
  - `scripts/portfolio.py`
  - `SKILL.md`
  - `README.md`

### `stock-rumors`

- GitHub: <https://github.com/baofeng-tech/agent-skills/tree/main/stock-rumors>
- Summary: Rumor Scanner — find early signals including M&A rumors, insider activity, analyst upgrades/downgrades, social whispers, and SEC/regulatory activity via AIsa API. Ranked by impact score. Use when the user asks about rumors, insider trading, M&A activity, analyst changes, or early market signals.
- Includes:
  - `scripts/rumor_scanner.py`
  - `SKILL.md`
  - `README.md`

### `stock-watchlist`

- GitHub: <https://github.com/baofeng-tech/agent-skills/tree/main/stock-watchlist>
- Summary: Manage a stock/crypto watchlist with price target and stop-loss alerts via AIsa API. Add, remove, list, and check tickers with live price alerts. Use when the user wants to track stocks, set price alerts, manage a watchlist, or check triggered alerts.
- Includes:
  - `scripts/watchlist.py`
  - `SKILL.md`
  - `README.md`

### `tavily-extract`

- GitHub: <https://github.com/baofeng-tech/agent-skills/tree/main/tavily-extract>
- Summary: Extract clean, readable content from one or more URLs using Tavily Extract via AIsa API. Useful for reading full articles without visiting the page. Use when: the user needs web search, research, source discovery, or content extraction.
- Includes:
  - `scripts/search_client.py`
  - `SKILL.md`
  - `README.md`

### `tavily-search`

- GitHub: <https://github.com/baofeng-tech/agent-skills/tree/main/tavily-search>
- Summary: Advanced web search via Tavily through AIsa API. Supports search depth, topic filtering (general/news/finance), time ranges, domain inclusion/exclusion, and LLM-generated answers. Use when: the user needs web search, research, source discovery, or content extraction.
- Includes:
  - `scripts/search_client.py`
  - `SKILL.md`
  - `README.md`

### `twitter`

- GitHub: <https://github.com/baofeng-tech/agent-skills/tree/main/twitter>
- Summary: Searches and reads X (Twitter): profiles, timelines, mentions, followers, tweet search, trends, lists, communities, and Spaces. Publishes posts, likes/unlikes tweets, and follows/unfollows users after the user completes OAuth in the browser. Use when the user asks about Twitter/X data, social listening, posting, or interacting with tweets/users without sharing account passwords.
- Includes:
  - `scripts/twitter_client.py`
  - `scripts/twitter_engagement_client.py`
  - `scripts/twitter_oauth_client.py`
  - `references/engage_twitter.md`
  - `references/post_twitter.md`

### `twitter-autopilot`

- GitHub: <https://github.com/baofeng-tech/agent-skills/tree/main/twitter-autopilot>
- Summary: Search and read X (Twitter) data via AIsa API: user profiles, timelines, mentions, followers, tweet search, trends, lists, communities, and Spaces. Publish posts, like/unlike tweets, and follow/unfollow users through OAuth relay — no passwords or cookies needed. Use when asked about Twitter/X data, social listening, influencer monitoring, trending topics, competitor intel, posting to X, or engaging with tweets.
- Includes:
  - `scripts/twitter_client.py`
  - `scripts/twitter_engagement_client.py`
  - `scripts/twitter_oauth_client.py`
  - `references/engage_twitter.md`
  - `references/post_twitter.md`

### `twitter-command-center-search-post`

- GitHub: <https://github.com/baofeng-tech/agent-skills/tree/main/twitter-command-center-search-post>
- Summary: Searches and reads X (Twitter): profiles, timelines, mentions, followers, tweet search, trends, lists, communities, and Spaces. Publishes posts after the user completes OAuth in the browser. Use when the user asks about Twitter/X data, social listening, or posting without sharing account passwords.
- Includes:
  - `scripts/twitter_client.py`
  - `scripts/twitter_oauth_client.py`
  - `references/post_twitter.md`
  - `SKILL.md`
  - `README.md`

### `twitter-command-center-search-post-interact`

- GitHub: <https://github.com/baofeng-tech/agent-skills/tree/main/twitter-command-center-search-post-interact>
- Summary: Searches and reads X (Twitter): profiles, timelines, mentions, followers, tweet search, trends, lists, communities, and Spaces. Publishes posts, likes/unlikes tweets, and follows/unfollows users after the user completes OAuth in the browser. Use when the user asks about Twitter/X data, social listening, posting, or interacting with tweets/users without sharing account passwords.
- Includes:
  - `scripts/twitter_client.py`
  - `scripts/twitter_engagement_client.py`
  - `scripts/twitter_oauth_client.py`
  - `references/engage_twitter.md`
  - `references/post_twitter.md`

### `us-stock-analyst`

- GitHub: <https://github.com/baofeng-tech/agent-skills/tree/main/us-stock-analyst>
- Summary: Professional US stock analysis with financial data, news, social sentiment, and multi-model AI. Comprehensive reports at $0.02-0.10 per analysis. Use when: the user needs market data, stock analysis, watchlists, or portfolio workflows.
- Includes:
  - `scripts/stock_analyst.py`
  - `scripts/test_api_data.py`
  - `requirements.txt`
  - `SKILL.md`
  - `README.md`

### `web-search`

- GitHub: <https://github.com/baofeng-tech/agent-skills/tree/main/web-search>
- Summary: Search the web using AIsa Scholar Web endpoint. Returns structured web results with titles, URLs, and snippets. Use when: the user needs web search, research, source discovery, or content extraction.
- Includes:
  - `scripts/search_client.py`
  - `SKILL.md`
  - `README.md`

### `x-intelligence-automation`

- GitHub: <https://github.com/baofeng-tech/agent-skills/tree/main/x-intelligence-automation>
- Summary: Search X/Twitter profiles, tweets, trends, and approved engagement actions through the AIsa relay. Use when the user asks for Twitter/X research, posting, likes, follows, or related workflows without sharing passwords.
- Includes:
  - `scripts/twitter_client.py`
  - `scripts/twitter_engagement_client.py`
  - `scripts/twitter_oauth_client.py`
  - `references/engage_twitter.md`
  - `references/post_twitter.md`

### `youtube`

- GitHub: <https://github.com/baofeng-tech/agent-skills/tree/main/youtube>
- Summary: YouTube SERP Scout for agents. Search top-ranking videos, channels, and trends for content research and competitor tracking. Use when: the user needs YouTube search, trend discovery, channel research, or SERP analysis.
- Includes:
  - `scripts/youtube_client.py`
  - `SKILL.md`
  - `README.md`

### `youtube-search`

- GitHub: <https://github.com/baofeng-tech/agent-skills/tree/main/youtube-search>
- Summary: YouTube Search API via AIsa unified endpoint. Search YouTube videos, channels, and playlists with a single AIsa API key — no Google API key or OAuth required. Use this skill when users want to search YouTube content. For other AIsa capabilities (LLM, financial data, Twitter, web search), see the aisa-core skill. Use when: the user needs YouTube search, trend discovery, channel research, or SERP analysis.
- Includes:
  - `SKILL.md`
  - `README.md`
