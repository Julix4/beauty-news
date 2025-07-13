# fmt: off

import json
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from goose3 import Goose
# import content_scripts.fetch_beauty...
import data.keywords as keywords
from content_scripts.fetch_beauty_news import fetch_beauty_news
from content_scripts.fetch_beauty_news_score import fetch_beauty_news_score

# Scraping beauty news
def scrape_beauty_news(url):
    g = Goose()
    article = g.extract(url)

    return {
        'title': article.title,
        'text': article.cleaned_text,  # [:150],
        'publish_date': article.publish_date
    }

# Test the script
if __name__ == "__main__":
    # Path JSON
    articles_path = "data/article_links_example.json"

    # Read and parsing JSON
    with open(articles_path, "r", encoding="utf-8") as file:
        articles = json.load(file)

    for i, article in enumerate(articles, start=0):
        article = scrape_beauty_news(articles[i]["link"])
        print(f"{i}. {article['title']}\n   Text: {article['text']}\n")
