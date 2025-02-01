from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils import load_draft_content, setup_driver


def draft_to_medium(driver, title, body):
    """Save a draft to Medium.
    """
    print("[Medium] Navigating to Medium 'New Story' page...")
    driver.get("https://medium.com/new-story")
    wait = WebDriverWait(driver, 10)

    # Wait for title field to appear
    print("[Medium] Waiting for title field...")
    title_input = wait.until(EC.presence_of_element_located(
        (By.XPATH, "//h3[@data-testid='editorTitleParagraph']")))

    # Add title
    print("[Medium] Adding title...")
    title_input.click()
    title_input.send_keys(title)

    # Add body
    print("[Medium] Adding body...")
    body_input = wait.until(EC.presence_of_element_located(
        (By.XPATH, "//p[@data-testid='editorParagraphText']")))
    body_input.click()
    body_input.send_keys(body)

    # Wait for autosave confirmation
    print("[Medium] Waiting for draft to be saved...")
    wait.until(EC.text_to_be_present_in_element(
        (By.XPATH, "//span[contains(text(), 'Saved')]"), "Saved"))

    print("[Medium] Draft saved successfully.")
