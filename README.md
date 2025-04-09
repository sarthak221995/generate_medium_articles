# 🧠 Generate Medium Article MCP Server

This project implements an MCP (Model Context Protocol) server using the `FastMCP` framework. The server exposes various tools for fetching search results, tweets, and Reddit posts via the Serper.dev API. These tools are designed to be orchestrated by a reasoning agent (e.g., a Claude desktop assistant) for generating SEO-optimized, high-quality Medium articles.

---

## 📌 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Exposed Tools](#exposed-tools)
- [Project Structure](#project-structure)
- [Claude Prompt Template](#claude-prompt-template)
- [License](#license)

---

## 🧾 Overview

This MCP server exposes three key tools:

1. `get_top_search_results`: Fetches top organic search results using the Serper.dev API.
2. `get_top_tweets_via_serper`: Simulates retrieval of relevant tweets using `site:x.com` filtering.
3. `get_top_reddit_posts`: Discovers top Reddit discussions using `site:reddit.com` queries.

These tools serve as content fetchers that allow AI agents to gather relevant, contextual information before composing articles.

---

## 🌟 Features

- 🔧 **Multi-tool content sourcing**
- 🔁 **Chain-of-thought friendly**
- 💡 **SEO-focused information retrieval**
- 🧵 **Compatible with Claude/Auto-GPT multi-agent workflows**
- 🔐 **Secure .env-based API key management**

---

## ⚙️ Requirements

- **Python 3.7+**
- Packages:
  - `mcp`
  - `requests`
  - `python-dotenv`

You will also need a **Serper.dev API key**.

---

## 🚀 Installation

```bash
# 1. Clone the repository
git clone https://github.com/your-username/generate_medium_article_mcp.git
cd generate_medium_article_mcp

# 2. (Optional) Set up a virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

🧪 Usage
bash
Copy
Edit
python main.py
This launches the MCP server on stdio transport. You can now integrate it with any MCP-compatible client or orchestrator.

🛠️ Exposed Tools
🔍 get_top_search_results(topic, limit=5)
Fetches top organic Google results via Serper.dev.

Returns: [{ title, url, snippet }]

🐦 get_top_tweets_via_serper(topic, limit=5)
Finds tweet-like content from X.com using Google site search.

Query format: site:x.com <topic>

🧵 get_top_reddit_posts(topic, limit=5)
Finds Reddit discussions using site:reddit.com via Serper.dev.

🧱 Project Structure
graphql
Copy
Edit
.
├── main.py               # MCP server implementation
├── utils.py              # Helper for API key retrieval
├── .env                  # Secret API key config
└── README.md             # This file
✨ Claude Prompt Template (Sample)
I need you to generate a comprehensive, SEO-friendly Medium article based on a given topic [TOPIC]. You will act as a multi-agent orchestrator using a chain-of-thought approach. Here’s how you should proceed:
1. **Article Structure and Planning (Structure Agent)**
   - First, analyze the provided title and generate an optimal article outline that fits SEO guidelines. Your outline should include sections such as:
     - Introduction
     - Background / History
     - Current Trends & Data
     - Social Media Insights (including tweet and Reddit highlights)
     - In-Depth Analysis (including expert opinions or case studies)
     - Conclusion & Future Perspectives
   - Describe briefly what each section will cover in terms of content focus and SEO keywords.
2. **Content Enrichment (Content Planner Agent)**
   - For each section of the outline, generate intermediate search queries by combining the section title with the main topic. For example, for the "Background" section, use a query like “Background on [Topic]” to fetch relevant data.
   - Call the search tool using these queries to get top search results (titles, URLs, and snippets) and incorporate the insights.
   - Summarize the findings in a coherent paragraph for each section. Ensure the content is in a natural, engaging tone that both informs the reader and satisfies SEO best practices.
3. **Social Media Insights**
   - Retrieve the latest and most relevant social media opinions about the topic.
     - Use the tweets tool to fetch popular tweets.
     - Use the Reddit posts tool to extract engaging discussions.
   - Summarize social sentiments and include direct links to a few key tweets and Reddit threads. Explain how these insights validate current trends or public opinions on the topic.
4. **Synthesis and Composition**
   - Based on the enriched outline and social media insights, compose a detailed draft of the Medium article in Markdown format.
   - Each section should have a clear header, well-developed paragraphs, and include calls to action where relevant (e.g., “Read more…” links).
   - Insert an editorial note at the end to make sure the article is SEO-optimized. This note can mention that keywords were naturally integrated and that the content has been structured for maximum reader engagement and search visibility.
5. **Final Editorial Pass (Editorial Agent)**
   - Perform a final review and editing pass on the article:
     - Smooth any rough transitions.
     - Verify that the tone is consistent and that the article reads naturally.
     - Add any final SEO meta-text (e.g., HTML comments with SEO guidelines) at the end.
   
Please show your complete reasoning along the way, listing which tools you are calling and how each piece of data (search results, tweet snippets, Reddit excerpts) is being used to build each section. Finally, output the complete Medium article in Markdown format.
**Topic/Title:** "[Insert the Article Title Here]"
Begin by outlining your plan and then proceed step by step. Each intermediate reasoning step is welcome. Use available tools (search, tweet, and Reddit queries) as necessary to inform your final article.

📄 License
MIT License © 2025

Made for orchestrated, intelligent article creation using agents + MCP + Serper.dev.