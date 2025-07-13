# fmt: off
"""
Run the following code to summarize news for creating new articles using the Gemini API.
Use 'pip install -q google-generativeai' to install the required package.
"""
import json
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from content_scripts.scrape_articles import scrape_beauty_news
import google.generativeai as genai


# Function for summarizing news
def summarize_news(articles):
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

    response = chat_session.send_message(
        "With these instructions:\n"
        "- The article should be 700-1000 words.\n" +
        "- Make sure not to add any brand or product name\n" +
        "- Only relevant information from the text provided, useful for marketing and the beauty community.\n\n" +
        "Summarize into one article for Medium the following articles:\n" + "\n".join([article for article in articles])
    )

    # Return the summarized news
    print(response.text)

# Function to convert response text to markdown format
def to_markdown(text):
    return f"### Summary\n\n{text}"


# Test the script
if __name__ == "__main__":
    # JSON file path
    article_links_path = "data/article_links_example.json"

# Read and parse the JSON
    with open(article_links_path, "r", encoding="utf-8") as file:
        article_links = json.load(file)

    articles = []

    for i, article in enumerate(article_links, start=0):
        article = scrape_beauty_news(article_links[i]["link"])
        articles.append(article['text'])
        print(f"{i}. {article['title']}\n   Text: {article['text']}\n")

        summarize_news(articles)
