import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from script.utils import load_draft_content, setup_driver


def save_to_substack(driver, title, body, subtitle=None):
    """Save a draft post to Substack from home page."""
    print("[Substack] Navigating to Substack homepage...")
    driver.get("https://substack.com/home")
    wait = WebDriverWait(driver, 10)

    # Click "Add" button
    print("[Substack] Clicking 'Add' button...")
    add_button = wait.until(EC.element_to_be_clickable((By.ID, "trigger3")))
    add_button.click()

    # Click "Post" option
    print("[Substack] Selecting 'Post' option...")
    post_option = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//a[contains(@href, '/publish/post')]")))
    post_option.click()

    # Wait for new post page to load
    print("[Substack] Waiting for new post page to load...")
    wait.until(EC.presence_of_element_located((By.ID, "post-title")))

    # Add title
    print("[Substack] Adding title...")
    title_input = driver.find_element(By.ID, "post-title")
    title_input.send_keys(title)

    # Add subtitle (optional)
    if subtitle:
        print("[Substack] Adding subtitle...")
        subtitle_input = driver.find_element(By.CLASS_NAME, "subtitle")
        subtitle_input.send_keys(subtitle)

    # Add body
    print("[Substack] Adding body...")
    body_input = driver.find_element(By.XPATH, "//div[@data-testid='editor']")
    body_input.click()
    body_input.send_keys(body)

    # Click back button to save draft
    print("[Substack] Saving draft...")
    back_button = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//button[contains(@class, 'iconButton2-DvFP7w')]")))
    back_button.click()

    # Click Dashboard button
    print("[Substack] Navigating to dashboard...")
    dashboard_button = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//button[@data-href and contains(text(), 'Dashboard')]")))
    dashboard_button.click()

    print("[Substack] Draft saved successfully.")
