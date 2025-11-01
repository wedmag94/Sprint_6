import allure

from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):
    @allure.step("Принять куки")
    def accept_cookies(self):
        self.click_to_element(MainPageLocators.COOKIES_BUTTON_LOCATOR)

    @allure.step("Дождаться видимости секции Вопросы о важном")
    def wait_for_element_faq(self):
        self.wait_for_element(MainPageLocators.FAQ_CONTAINER)

    @allure.step("Кликнуть на вопрос")
    def click_on_faq_number(self, faq_number):
        faq_locator = MainPageLocators.faq_question(faq_number)
        self.scroll_to_element(faq_locator)
        self.click_to_element(faq_locator)

    @allure.step("Сравнить ответ на вопрос")
    def check_the_answer_to_the_question(self, answer_number, expected_text):
        answer_locator = MainPageLocators.answer_number(answer_number)
        actual_text = self.get_text_on_element(answer_locator)
        return actual_text == expected_text

    @allure.step("Нажать кнопку Заказать")
    def button_order_click(self, button):
        if button == "top":
            self.click_to_element(MainPageLocators.BUTTON_ORDER_TOP)
        elif button == "bottom":
            self.click_to_element(MainPageLocators.BUTTON_ORDER_BOTTOM)

    @allure.step("Кликнуть на логотип Самокат")
    def click_logo_scooter(self):
        self.click_to_element(MainPageLocators.LOGO_SCOOTER)

    @allure.step("Кликнуть на логотип Яндекс и перейти в новое окно")
    def click_logo_yandex(self):
        self.click_to_element(MainPageLocators.LOGO_YANDEX)
        self.switch_to_new_window()
        self.wait_dzen()
