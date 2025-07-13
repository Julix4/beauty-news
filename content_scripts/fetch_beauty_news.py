# Import libraries
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import data.keywords as keywords
from dotenv import load_dotenv
import requests
import json
from datetime import datetime

load_dotenv()


def fetch_beauty_news(api_key, keywords, num_articles=6):
    url = "https://serpapi.com/search"
    params = {
        "engine": "google_news",
        "q": " OR ".join(keywords),
        "api_key": api_key,
        "hl": "en",
        "gl": "us",
        "cr": "countryGB|countryUS|countryAU|countryCA",
        "device": "desktop",
        "tbm": "nws",
        "tbs": "qdr:d"
    }

    response = requests.get(url, params=params)
    if response.status_code != 200:
        print("Failed to fetch news.")
        return []

    news_data = response.json().get("news_results", [])

    # Filter articles by recency and relevance (if necessary)
    filtered_articles = [
        {
            "title": article["title"],
            "link": article["link"],
            "source": article["source"],
            "published": article["date"],
            "position": article["position"],
        }
        for article in news_data
        if "beauty" in article["title"].lower() or any(kw in article["title"].lower() for kw in keywords)
    ]

    # Sort by publication date
    sorted_articles = sorted(
        filtered_articles, key=lambda x: x["position"]
    )

    return sorted_articles[:num_articles]


# Test the script
if __name__ == "__main__":
    API_KEY = os.environ.get("GOOGLE_API_KEY")
    if not API_KEY:
        print("Error: GOOGLE_API_KEY not found in environment variables")
        exit(1)

    KEYWORDS = keywords.KEYWORDS["news"]
    print(f"Fetching beauty news with keywords: {KEYWORDS}")

    articles = fetch_beauty_news(API_KEY, KEYWORDS)

    if articles:
        print(f"\nFound {len(articles)} articles:")
        for i, article in enumerate(articles, start=1):
            print(f"{i}. {article['title']}")
            print(f"   Source: {article['source']}")
            print(f"   Published: {article['published']}")
            print(f"   Link: {article['link']}\n")
    else:
        print("No articles found.")
