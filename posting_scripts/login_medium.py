# Import necessary libraries and modules
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from utils import MEDIUM_EMAIL, MEDIUM_PASSWORD, setup_driver

# Function to log in to Medium


def login_to_medium(driver):
    """""""""""
    Log in to Medium using the provided email and password.
    It will ask for manual input of the email verification code.
    :param driver: Selenium WebDriver object
    :return: None
    """""""""""
    try:
        print("[Medium] Navigating to Medium login page...")
        driver.get("https://medium.com/m/signin")
        wait = WebDriverWait(driver, 10)

        # Click "Sign in with email"
        print("[Medium] Clicking 'Sign in with email' button...")
        email_signin = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//button[contains(., 'Sign in with email')]")))
        email_signin.click()

        # Input email
        print("[Medium] Waiting for email input field...")
        email_field = wait.until(EC.presence_of_element_located(
            (By.XPATH, "//input[@type='email']")))
        email_field.send_keys(MEDIUM_EMAIL)

        # Click "Continue" button
        print("[Medium] Clicking 'Continue' button after entering email...")
        continue_button = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//button[contains(text(), 'Continue')]")))
        continue_button.click()

        # Ask for email verification code or link and wait for manual input
        print("[Medium] Waiting for user to input email verification code or link...")
        time.sleep(20)

        # Confirm successful login by waiting for "Write" label
        wait.until(EC.presence_of_element_located(
            (By.XPATH, "//div[contains(text(), 'Write')]")))

        print("[Medium] Logged in to Medium successfully.")
    except TimeoutException as e:
        print("[Medium] Error: Timeout while logging in to Medium.")
        print(f"Details: {str(e)}")
    except NoSuchElementException as e:
        print("[Medium] Error: Unable to locate an element while logging in to Medium.")
        print(f"Details: {str(e)}")
