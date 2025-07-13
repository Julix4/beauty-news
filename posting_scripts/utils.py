import json
import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Credentials
MEDIUM_EMAIL = os.getenv("MEDIUM_EMAIL")
MEDIUM_PASSWORD = os.getenv("MEDIUM_PASSWORD")
SUBSTACK_EMAIL = os.getenv("SUBSTACK_EMAIL")
SUBSTACK_PASSWORD = os.getenv("SUBSTACK_PASSWORD")


def setup_driver(headless=True):
    """Initialize and return a Selenium WebDriver instance."""
    options = Options()
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--start-maximized")

    service = Service(path='./chromedriver')  # Adjust if necessary
    driver = webdriver.Chrome(service=service, options=options)
    wait = WebDriverWait(driver, 30)  # Set explicit wait time
    return driver


def load_draft_content(json_file):
    """Load content from a JSON file with a relative path."""
    base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    json_path = os.path.join(base_path, json_file)
    with open(json_path, "r", encoding="utf-8") as file:
        return json.load(file)
