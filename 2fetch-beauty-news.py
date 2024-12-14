# Import libraries
# Create function for news fetch
import requests
import json
from datetime import datetime


def fetch_beauty_news(api_key, keywords, num_articles=6):
    url = "https://serpapi.com/search"
    params = {
        "engine": "google_news",
        "q": " OR ".join(keywords),
        "api_key": api_key,
        "hl": "en",
        "gl": "us",
        "cr": "countryGB|countryUS",
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
    today = datetime.now().date()
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


# Example Usage

API_KEY = "69e6ac0bc7a9e0c6e06a5ff9a4bc5b2d462019279d80e08aa4802800c45eae6c"
# KEYWORDS = ["beauty", "skincare", "makeup", "cosmetics", "technology"]
KEYWORDS = ["beauty trends", "skincare", "makeup", "cosmetics", "beauty tech"]

articles = fetch_beauty_news(API_KEY, KEYWORDS)

for i, article in enumerate(articles, start=1):
    print(
        f"{i}. {article['title']}\n   Source: {article['source']}\n   Published: {article['published']}\n   Link: {article['link']}\n")
