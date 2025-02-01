import os
import time
from dotenv import load_dotenv
from selenium import webdriver
from utils import load_draft_content
from save_substack_draft import save_to_substack
from save_medium_draft import draft_to_medium

# Load environment variables
load_dotenv()

# Get Chrome profile path from .env
CHROME_PROFILE_PATH = os.getenv("CHROME_PROFILE_PATH")


def setup_driver():
    """Sets up a persistent Chrome WebDriver session using the existing user profile."""
    options = webdriver.ChromeOptions()

    # Use existing Chrome session
    options.add_argument(f"user-data-dir={CHROME_PROFILE_PATH}")

    # Avoid loading images for faster performance
    prefs = {"profile.managed_default_content_settings.images": 2}
    options.add_experimental_option("prefs", prefs)

    # Start WebDriver
    driver = webdriver.Chrome(options=options)
    return driver


if __name__ == "__main__":
    driver = setup_driver()
    drafts = load_draft_content("data/draft_content_example.json")

    try:
        for draft in drafts:
            platform = draft.get("platform_name").lower()
            title = draft["title"]
            body = draft["body"]

            if platform == "substack":
                print(f"[Substack] Processing draft: {title}")
                save_to_substack(driver, title, body, draft.get("subtitle"))

            elif platform == "medium":
                print(f"[Medium] Processing draft: {title}")
                draft_to_medium(driver, title, body)

    except Exception as e:
        print(f"[Error] {e}")

    # Keep the browser open
    print("[INFO] All drafts processed. The browser will remain open for manual checks.")
    while True:
        time.sleep(60)
