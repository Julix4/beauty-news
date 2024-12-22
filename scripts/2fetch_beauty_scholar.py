# Import libraries
# Create function for news fetch
import data.keywords as keywords
import os
from datetime import datetime
import json
import requests
from dotenv import load_dotenv
load_dotenv()


def fetch_beauty_scholar(api_key, keywords, num_articles=2):
    url = "https://serpapi.com/search"
    params = {
        "engine": "google_scholar",
        "q": " OR ".join(keywords),
        "api_key": api_key,
        "hl": "en",
        "as_ylo": "2024",
        "scisbd": "2"
    }

    response = requests.get(url, params=params)
    if response.status_code != 200:
        print('response:', response)
        print("Failed to fetch news.")
        return []

    news_data = response.json().get("organic_results", [])

    # Filter articles by recency and relevance (if necessary)
    today = datetime.now().date()
    filtered_articles = [
        {
            "title": article["title"],
            "link": article["link"],
            "position": article["position"],
        }
        for article in news_data
        if any(kw in article["link"].lower() for kw in keywords)
    ]

    # Sort by publication date
    sorted_articles = sorted(
        filtered_articles, key=lambda x: x["position"]
    )

    return sorted_articles[:num_articles]


# Example Usage
API_KEY = os.environ["GOOGLE_API_KEY"]
KEYWORDS = keywords.KEYWORDS["scholar"]
articles = fetch_beauty_scholar(API_KEY, KEYWORDS)

for i, article in enumerate(articles, start=1):
    print(
        f"{i}. {article['title']}\n   Link: {article['link']}\n")
