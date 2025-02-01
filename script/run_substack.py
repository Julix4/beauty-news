from selenium.webdriver.common.by import By
import time
from utils import setup_driver
from login_medium import login_to_medium
from login_substack import login_to_substack
from save_medium_draft import draft_to_medium
from save_substack_draft import save_to_substack
from utils import load_draft_content


def run_substack():
    driver = setup_driver(headless=False)  # Start single browser session
    driver.get("https://substack.com/")  # Open Medium in first tab

    # Log in Substack tab and log in
    login_to_substack(driver)

    # Load drafts
    drafts = load_draft_content("data/draft_content_example.json")

    # Process Substack drafts
    for draft in drafts:
        if draft.get("platform_name", "").lower() == "substack":
            save_to_substack(driver, draft["title"], draft["body"], draft.get(
                "subtitle"))

    print("[INFO] Run completed. Tabs remain open for review.")


if __name__ == "__main__":
    run_substack()
