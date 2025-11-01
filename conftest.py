import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from pages.main_page import MainPage


from curl import *


@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--window-size=1200,600")
    driver = webdriver.Firefox(options=options)
    driver.get(main_site)

    main_page = MainPage(driver)
    main_page.accept_cookies()

    yield driver
    driver.quit()
