import allure
from pages.main_page import MainPage
from curl import *


class TestLogo:

    @allure.title("Тестирование клика на логотип Самокат")
    def test_logo_scooter(self, driver):
        main_page = MainPage(driver)
        main_page.button_order_click(button="top")
        main_page.click_logo_scooter()
        assert main_page.get_current_url() == main_site

    @allure.title("Тестирование клика на логотип Яндекс")
    def test_logo_yandex(self, driver):
        main_page = MainPage(driver)
        main_page.click_logo_yandex()
        assert main_page.get_current_url() == yandex_dzen
