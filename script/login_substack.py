# Load libraries
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from utils import SUBSTACK_EMAIL, SUBSTACK_PASSWORD, setup_driver

# Function to log in to Substack


def login_to_substack(driver):
    """""""""""
    Log in to Substack using the provided email and password.
    It will ask for manual input of the email verification link or code.
    :param driver: Selenium WebDriver object
    :return: None
    """""""""""
    try:
        print("[Substack] Navigating to Substack login page...")
        driver.get("https://substack.com/sign-in")
        wait = WebDriverWait(driver, 10)

        # Click "Sign in with password"
        print("[Substack] Clicking 'Sign in with password' link...")
        password_signin = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//a[@class='login-option substack-login__login-option']")))
        password_signin.click()

        # Input email
        print("[Substack] Waiting for email input field...")
        email_field = wait.until(EC.presence_of_element_located(
            (By.XPATH, "//input[@type='email' and @name='email']")))
        email_field.send_keys(SUBSTACK_EMAIL)

        # Input password
        print("[Substack] Waiting for password input field...")
        password_field = wait.until(EC.presence_of_element_located(
            (By.XPATH, "//input[@type='password' and @name='password']")))
        password_field.send_keys(SUBSTACK_PASSWORD)

        # Click "Continue" button
        print("[Substack] Clicking 'Continue' button...")
        continue_button = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//button[contains(text(), 'Continue')]")))
        continue_button.click()
        # time.sleep(5)

        # Confirm successful login by waiting for "dashboard" button
        wait.until(EC.presence_of_element_located(
            (By.XPATH, "//button[contains(text(), 'Dashboard')]")))

        print("[Substack] Logged in to Substack successfully.")
    except (TimeoutException, NoSuchElementException) as e:
        print(f"[Substack] [ERROR] Substack login failed: {e}")
        raise
