# fmt: off
"""
Run the following code to summarize news for creating new articles using the Gemini API.
Use 'pip install -q google-generativeai' to install the required package.
"""
import json
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from scripts.scrape_articles import scrape_beauty_news
import google.generativeai as genai

# Function for summarizing news for a specific platform
def summarize_news_for_platform(articles, platform, article_length, additional_instructions=""):
    # Use the API to create an article
    genai.configure(api_key=os.environ["GEMINI_API_KEY"])

    # Create the model
    generation_config = {
        "temperature": 1,
        "top_p": 0.95,
        "top_k": 40,
        "max_output_tokens": 8192,
        "response_mime_type": "text/plain",
    }

    model = genai.GenerativeModel(
        model_name="gemini-2.0-flash-exp",
        generation_config=generation_config,
    )

    chat_session = model.start_chat(history=[])

    # Platform-specific instructions
    instructions = (
        f"With these instructions:\n- The article should be {article_length} words.\n"
        "- Make sure not to add any brand or product name.\n"
        "- Only relevant information from the text provided, useful for marketing and the beauty community.\n"
        f"- Tailored for publishing on {platform}.\n{additional_instructions}\n\n"
        "Summarize into one article the following articles:\n"
        + "\n".join(articles)
    )

    response = chat_session.send_message(instructions)

    # Return the summarized news
    print(f"\n=== {platform} Article ===\n")
    print(response.text)
    return response.text


# Main script logic

# Path to the JSON file
article_links_path = "data/article_links_example.json"

# Read and parse the JSON
with open(article_links_path, "r", encoding="utf-8") as file:
    article_links = json.load(file)

articles = []

for i, article in enumerate(article_links, start=0):
    article = scrape_beauty_news(article_links[i]["link"])
    articles.append(article['text'])
    print(f"{i}. {article['title']}\n   Text: {article['text']}\n")

# Split articles for Medium and Substack
medium_articles = articles[:4]  # First 3-4 articles
substack_articles = articles[4:7]  # Next 2-3 articles

# Summarize for Medium
medium_summary = summarize_news_for_platform(
    medium_articles,
    platform="Medium",
    article_length="700-1000"
)

# Summarize for Substack
substack_summary = summarize_news_for_platform(
    substack_articles,
    platform="Substack",
    article_length="500-700"
)