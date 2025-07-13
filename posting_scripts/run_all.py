from selenium.webdriver.common.by import By
import time
from utils import setup_driver
from login_medium import login_to_medium
from login_substack import login_to_substack
from publish_medium import publish_medium
from publish_substack import publish_substack
from run_medium import run_medium
from run_substack import run_substack
from utils import load_draft_content


def run_all():
    run_medium()
    run_substack()


if __name__ == "__main__":
    run_all()
