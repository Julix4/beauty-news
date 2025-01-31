from selenium.webdriver.common.by import By
import time
from script.utils import setup_driver
from script.login_medium import login_to_medium
from script.login_substack import login_to_substack
from script.save_medium_draft import draft_to_medium
from script.save_substack_draft import save_to_substack
from script.utils import load_draft_content


def run_all():
    driver = setup_driver(headless=False)  # Start single browser session
    driver.get("https://medium.com/")  # Open Medium in first tab
    time.sleep(2)
    # Open Substack in new tab
    driver.execute_script("window.open('https://substack.com/','_blank');")
    time.sleep(2)

    # Switch to Medium tab and log in
    driver.switch_to.window(driver.window_handles[0])
    login_to_medium(driver)

    # Switch to Substack tab and log in
    driver.switch_to.window(driver.window_handles[1])
    login_to_substack(driver)

    # Load drafts
    drafts = load_draft_content("data/draft_content_example.json")

    # Process Medium drafts
    driver.switch_to.window(driver.window_handles[0])  # Switch to Medium tab
    for draft in drafts:
        if draft.get("platform_name", "").lower() == "medium":
            draft_to_medium(driver, draft["title"], draft["body"])

    # Process Substack drafts
    driver.switch_to.window(driver.window_handles[1])  # Switch to Substack tab
    for draft in drafts:
        if draft.get("platform_name", "").lower() == "substack":
            save_to_substack(driver, draft["title"], draft["body"], draft.get(
                "tags"), draft.get("summary"), draft.get("audience"))

    print("[INFO] Run completed. Tabs remain open for review.")


if __name__ == "__main__":
    run_all()
