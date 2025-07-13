import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from utils import load_draft_content, setup_driver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def publish_medium(driver, title, body, tags):
    """Publish to Medium.
    Args:
        driver: Selenium WebDriver instance.
        title: Post title.
        body: Post body.
        tags: List of tags.
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

    # Publish draft
    print("[Medium] Publishing draft...")
    publish_button = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//button[contains(@class, 'js-publishButton')]")))
    publish_button.click()

    # Add tags (if provided)
    if tags:
        print(f"[Medium] Adding tags...")
        tags_input = wait.until(EC.presence_of_element_located(
            (By.XPATH, "//div[@data-testid='publishTopicsInput']")))
        tags_input.click()

        for tag in tags:
            tags_input.send_keys(tag)
            tags_input.send_keys(Keys.ENTER)
            time.sleep(1)

    driver.find_element(By.TAG_NAME, "body").click()

    # Publish now
    print("[Medium] Publishing now...")
    publish_now_button = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//button[@data-action='publish' and contains(@class, 'js-publishButton')]")))
    publish_now_button.click()
    time.sleep(2)

    # Wait for confirmation
    print("[Medium] Content Published!")
