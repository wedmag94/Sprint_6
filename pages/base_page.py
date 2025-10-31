import allure

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from curl import *


class BasePage:

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.timeout = timeout

    @allure.step("Подождать видимости элемента")
    def wait_for_element(self, locator):
        return WebDriverWait(self.driver, self.timeout).until(
            EC.visibility_of_element_located(locator)
        )

    @allure.step("Подождать кликабельность элемента")
    def wait_element_to_be_clickable(self, locator):
        return WebDriverWait(self.driver, self.timeout).until(
            EC.element_to_be_clickable(locator)
        )

    @allure.step("Скролл до элемента")
    def scroll_to_element(self, locator):
        element = self.wait_for_element(locator)
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center', inline: 'nearest'});",
            element,
        )

    @allure.step("Кликнуть на элемент")
    def click_to_element(self, locator):
        element = self.wait_element_to_be_clickable(locator)
        self.scroll_to_element(locator)
        element.click()

    @allure.step("Ввести текст в поле ввода")
    def send_keys_to_input(self, locator, keys):
        element = self.wait_for_element(locator)
        element.clear()
        element.send_keys(keys)

    @allure.step("Получить текст элемента")
    def get_text_on_element(self, locator):
        element = self.wait_for_element(locator)
        return element.text

    @allure.step("Подождать и проверить, что атрибут элемента содержит текст")
    def wait_for_attribute(self, locator, attribute, value):
        return WebDriverWait(self.driver, self.timeout).until(
            EC.text_to_be_present_in_element_attribute(locator, attribute, value)
        )

    @allure.step("Переключиться на новое окно")
    def switch_to_new_window(self):
        WebDriverWait(self.driver, self.timeout).until(EC.number_of_windows_to_be(2))
        self.driver.switch_to.window(self.driver.window_handles[1])

    @allure.step("Ожидание загрузки страницы Дзена")
    def wait_dzen(self):
        WebDriverWait(self.driver, self.timeout).until(EC.url_to_be(yandex_dzen))
