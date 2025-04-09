from mcp.server.fastmcp import FastMCP
import csv
from dotenv import load_dotenv
import os
from utils import get_openai_api_key, get_serper_api_key
import requests
# Create an MCP server instance with a chosen name.
mcp = FastMCP("generate_medium_article")

SERPER_API_KEY = get_serper_api_key()


@mcp.tool()
def get_top_search_results(topic, limit='5'):
    """
    Fetches the top organic search results for a given topic using the Serper.dev API.

    This function sends a POST request to the Serper.dev Google Search API with the specified topic
    and returns a list of dictionaries containing the title, URL, and snippet for each result.

    Args:
        topic (str): The search query or topic to retrieve results for.
        limit (int, optional): The maximum number of search results to return. Default is 5.

    Returns:
        List[dict]: A list of search results, where each result is a dictionary with the keys:
            - 'title': The title of the search result.
            - 'url': The URL of the result.
            - 'snippet': A short description or snippet from the result.
    """
    try:
        limit = int(limit)
    except ValueError:
        limit = 5
    url = "https://google.serper.dev/search"
    headers = {
        "X-API-KEY": SERPER_API_KEY,
        "Content-Type": "application/json"
    }
    payload = {"q": topic}

    response = requests.post(url, headers=headers, json=payload)
    results = response.json()

    search_results = []
    for item in results.get("organic", [])[:limit]:
        search_results.append({
            "title": item.get("title"),
            "url": item.get("link"),
            "snippet": item.get("snippet")
        })
    return search_results


@mcp.tool()
def get_top_tweets_via_serper(topic, limit='5'):
    """
    Retrieves top publicly visible tweets related to a given topic using the Serper.dev API.

    This function leverages Google's search capabilities via the Serper.dev API to simulate
    tweet discovery by querying for tweets on X.com (formerly Twitter). It constructs a search
    query with the "site:x.com" filter to fetch relevant tweet links and metadata.

    Args:
        topic (str): The topic or keyword to search tweets for.
        limit (int, optional): The maximum number of tweet results to return. Default is 5.

    Returns:
        List[dict]: A list of tweet-like results, where each result is a dictionary containing:
            - 'title': The title of the tweet or page (as returned by the search engine).
            - 'url': The direct URL to the tweet on X.com.
            - 'snippet': A preview text or snippet from the tweet content.
    """
    try:
        limit = int(limit)
    except ValueError:
        limit = 5
    query = f"site:x.com {topic}"
    url = "https://google.serper.dev/search"
    headers = {
        "X-API-KEY": SERPER_API_KEY,
        "Content-Type": "application/json"
    }
    payload = {"q": query}

    response = requests.post(url, headers=headers, json=payload)
    results = response.json()

    tweets = []
    for item in results.get("organic", [])[:limit]:
        tweets.append({
            "title": item.get("title"),
            "url": item.get("link"),
            "snippet": item.get("snippet")
        })
    return tweets



@mcp.tool()
def get_top_reddit_posts(topic, limit='5'):
    """
    Retrieves top Reddit posts related to a given topic using the Serper.dev API.

    This function uses Google's search engine through Serper.dev to find public Reddit
    posts or discussions by including the "site:reddit.com" filter in the query.

    Args:
        topic (str): The search term or topic to look up on Reddit.
        limit (int, optional): The maximum number of Reddit posts to return. Default is 5.

    Returns:
        List[dict]: A list of Reddit results, where each result is a dictionary with:
            - 'title': The post title or page title.
            - 'url': Direct URL to the Reddit post or thread.
            - 'snippet': A short snippet or preview of the post.
    """
    try:
        limit = int(limit)
    except ValueError:
        limit = 5
    query = f"site:reddit.com {topic}"
    url = "https://google.serper.dev/search"
    headers = {
        "X-API-KEY": SERPER_API_KEY,
        "Content-Type": "application/json"
    }
    payload = {"q": query}

    response = requests.post(url, headers=headers, json=payload)
    results = response.json()

    reddit_posts = []
    for item in results.get("organic", [])[:limit]:
        reddit_posts.append({
            "title": item.get("title"),
            "url": item.get("link"),
            "snippet": item.get("snippet")
        })
    return reddit_posts


if __name__ == "__main__":
    # Run the server using the stdio transport. This means it listens for requests on standard I/O.
    mcp.run(transport="stdio")
