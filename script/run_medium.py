import time
from login_medium import login_to_medium
from publish_medium import publish_medium
from selenium.webdriver.common.by import By
from utils import setup_driver, load_draft_content


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
            publish_medium(driver, draft["title"],
                           draft["body"], draft["tags"])

    print("[Medium] Run completed.")


if __name__ == "__main__":
    run_medium()
