import logging
import time
import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver
from pages.login_page import LoginPage
from pages.inventory_page import Inventory
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


# Set up logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)
    

@pytest.fixture(scope="module")
def driver():
    logger.info("Step 1: Open the browser")
    print("Step 1: Open the browser")
    options = Options()
    options.add_argument("--incognito")
    service = ChromeService(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.maximize_window()
    yield driver
    driver.quit()  