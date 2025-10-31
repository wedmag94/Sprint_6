import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from locators.main_page_locators import MainPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from curl import *


@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--window-size=1200,600")
    driver = webdriver.Firefox(options=options)
    driver.get(main_site)
    accept_cookies(driver)

    yield driver
    driver.quit()


def accept_cookies(driver):
    cookies = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(MainPageLocators.COOKIES_BUTTON_LOCATOR)
    )
    cookies.click()
