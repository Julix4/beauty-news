from selenium.webdriver.common.by import By
import time
from utils import setup_driver
from login_medium import login_to_medium
from login_substack import login_to_substack
from save_medium_draft import draft_to_medium
from save_substack_draft import save_to_substack
from utils import load_draft_content


def run_medium():
    driver = setup_driver(headless=False)  # Start single browser session
    driver.get("https://medium.com/")  # Open Medium in first tab
    time.sleep(4)

    # log in to Medium
    login_to_medium(driver)

    # Load drafts
    drafts = load_draft_content("data/draft_content_example.json")

    # Process Medium drafts
    for draft in drafts:
        if draft.get("platform_name", "").lower() == "medium":
            draft_to_medium(driver, draft["title"], draft["body"])

    print("[Medium] Run completed.")


if __name__ == "__main__":
    run_medium()
