# fmt: off

import json
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from goose3 import Goose
# import scripts.fetch_beauty...
import data.keywords as keywords
from scripts.fetch_beauty_news import fetch_beauty_news
from scripts.fetch_beauty_scholar import fetch_beauty_scholar

# Scraping beauty news


def scrape_beauty_news(url):
    g = Goose()
    article = g.extract(url)

    return {
        'title': article.title,
        'text': article.cleaned_text,  # [:150],
        'publish_date': article.publish_date
    }


""" API_KEY = os.environ["GOOGLE_API_KEY"]
KEYWORDS = keywords.KEYWORDS["news"]
articles = fetch_beauty_news(API_KEY, KEYWORDS) """

# Ruta al archivo JSON
articles_path = "data/article_links_example.json"

# Leer y parsear el JSON
with open(articles_path, "r", encoding="utf-8") as file:
    articles = json.load(file)

for i, article in enumerate(articles, start=0):
    article = scrape_beauty_news(articles[i]["link"])
    print(f"{i}. {article['title']}\n   Text: {article['text']}\n")
