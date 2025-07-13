from selenium.webdriver.common.by import By
from login_substack import login_to_substack
from publish_substack import publish_substack
from utils import setup_driver, load_draft_content


def run_substack():
    driver = setup_driver(headless=False)  # Start single browser session
    driver.get("https://substack.com/")

    # Log in Substack tab and log in
    login_to_substack(driver)

    # Load drafts
    drafts = load_draft_content("data/draft_content_example.json")

    # Process Substack drafts
    for draft in drafts:
        if draft.get("platform_name", "").lower() == "substack":
            publish_substack(
                driver, draft["title"], draft["body"], draft["tags"], draft.get("subtitle"))


if __name__ == "__main__":
    run_substack()
