# Import necessary libraries and modules
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from script.utils import MEDIUM_EMAIL, MEDIUM_PASSWORD, setup_driver

# Function to log in to Medium


def login_to_medium(driver):
    """""""""""
    Log in to Medium using the provided email and password.
    It will ask for manual input of the email verification code.
    :param driver: Selenium WebDriver object
    :return: None
    """""""""""
    try:
        print("Navigating to Medium login page...")
        driver.get("https://medium.com/m/signin")
        wait = WebDriverWait(driver, 10)
        time.sleep(2)

        # Click "Sign in with email"
        print("Clicking 'Sign in with email' button...")
        email_signin = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//button[contains(., 'Sign in with email')]")))
        email_signin.click()
        time.sleep(2)

        # Input email
        print("Waiting for email input field...")
        email_field = wait.until(EC.presence_of_element_located(
            (By.XPATH, "//input[@type='email']")))
        email_field.send_keys(MEDIUM_EMAIL)

        # Click "Continue" button
        print("Clicking 'Continue' button after entering email...")
        continue_button = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//button[contains(text(), 'Continue')]")))
        continue_button.click()
        time.sleep(2)

        # Ask for email verification code and wait for manual input
        print("Waiting for user to input email verification code...")
        verification_ok_button = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//button[contains(text(), 'OK')]")))
        verification_ok_button.click()
        time.sleep(5)

        print("Logged in to Medium successfully.")
    except TimeoutException as e:
        print("Error: Timeout while logging in to Medium.")
        print(f"Details: {str(e)}")
    except NoSuchElementException as e:
        print("Error: Unable to locate an element while logging in to Medium.")
        print(f"Details: {str(e)}")
