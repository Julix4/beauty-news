# Create function for news fetch
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import data.keywords as keywords
from dotenv import load_dotenv
import requests
import json
from datetime import datetime


def fetch_beauty_news_score(api_key, keywords, preferred_sources, num_articles=6):
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

    # Filter and score articles
    def score_article(article):
        source_url = article["link"].lower()
        priority_score = sum(src in source_url for src in preferred_sources)
        return priority_score * 10

    filtered_articles = [
        {
            "title": article["title"],
            "link": article["link"],
            "source": article["source"],
            "published": article["date"],
            "score": score_article(article)
        }
        for article in news_data
        if any(kw in article["title"].lower() for kw in keywords)
    ]

    # Sort by score
    sorted_articles = sorted(
        filtered_articles, key=lambda x: x["score"], reverse=True
    )

    return sorted_articles[:num_articles]


# Test the script
if __name__ == "__main__":
    KEYWORDS = keywords.KEYWORDS["news"]
    PREFERRED_SOURCES = [
    "theindustry.beauty", "businessoffashion.com", "glossy.co",
    "whowhatwear.com", "women.com", "allure.com",
    "marieclaire.co.uk", "vogue.co.uk", "vogue.com", "marieclaire.com",
    "women.co.uk"
    ]
    API_KEY = os.environ["GOOGLE_API_KEY"]
    articles = fetch_beauty_news_score(API_KEY, KEYWORDS, PREFERRED_SOURCES)

    for i, article in enumerate(articles, start=1):
        print(
            f"{i}. {article['title']}\n   Source: {article['source']}\n   Published: {article['published']}\n   Link: {article['link']}\n")
